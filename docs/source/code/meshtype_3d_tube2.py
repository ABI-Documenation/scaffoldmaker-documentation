"""
Generates a 3-D unit tube mesh with variable numbers of elements around, along and
through wall, plus variable wall thickness for unit diameter.
"""

#DOC-START imports
from __future__ import division
import math
from opencmiss.utils.zinc.field import findOrCreateFieldCoordinates
from opencmiss.zinc.element import Element, Elementbasis
from opencmiss.zinc.field import Field
from opencmiss.zinc.node import Node
from scaffoldmaker.meshtypes.scaffold_base import Scaffold_base
from scaffoldmaker.utils.eftfactory_tricubichermite import eftfactory_tricubichermite
#DOC-END imports

#DOC-START create class
class MeshType_3d_tube2(Scaffold_base):
    @staticmethod
    def getName():
        return '3D Tube 2'

    #options
    @staticmethod
    def getDefaultOptions(parameterSetName='Default'):
        return {
            'Number of elements around': 4,
            'Number of elements along': 2,
            'Number of elements through wall': 1,
            'Wall thickness': 0.25,
            'Inside radius': 0.25,
            'Use cross derivatives': False,
        }

    @staticmethod
    def getOrderedOptionNames():
        return [
            'Number of elements around',
            'Number of elements along',
            'Number of elements through wall',
            'Wall thickness',
            'Tube length',
            'Use cross derivatives',
        ]

    @staticmethod
    def checkOptions(options):
        for key in [
            'Number of elements along',
            'Number of elements through wall']:
            if options[key] < 1:
                options[key] = 1
        if (options['Number of elements around'] < 3):
            options['Number of elements around'] = 3
        if (options['Wall thickness'] < 0.0):
            options['Wall thickness'] = 0.0
        elif (options['Wall thickness'] > 0.5):
            options['Wall thickness'] = 0.5
    # generate mesh
    @classmethod
    def generateBaseMesh(cls, region, options):
        elementsCountAround = options['Number of elements around']
        elementsCountAlong = options['Number of elements along']
        elementsCountThroughWall = options['Number of elements through wall']
        wallThickness = options['Wall thickness']
        useCrossDerivatives = options['Use cross derivatives']

        fm = region.getFieldmodule()
        fm.beginChange()
        coordinates = findOrCreateFieldCoordinates(fm)

        nodes = fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        nodetemplate = nodes.createNodetemplate()
        nodetemplate.defineField(coordinates)
        nodetemplate.setValueNumberOfVersions(coordinates, -1, Node.VALUE_LABEL_VALUE, 1)
        nodetemplate.setValueNumberOfVersions(coordinates, -1, Node.VALUE_LABEL_D_DS1, 1)
        nodetemplate.setValueNumberOfVersions(coordinates, -1, Node.VALUE_LABEL_D_DS2, 1)
        nodetemplate.setValueNumberOfVersions(coordinates, -1, Node.VALUE_LABEL_D_DS3, 1)
        if useCrossDerivatives:
            nodetemplate.setValueNumberOfVersions(coordinates, -1, Node.VALUE_LABEL_D2_DS1DS2, 1)
            nodetemplate.setValueNumberOfVersions(coordinates, -1, Node.VALUE_LABEL_D2_DS1DS3, 1)
            nodetemplate.setValueNumberOfVersions(coordinates, -1, Node.VALUE_LABEL_D2_DS2DS3, 1)
            nodetemplate.setValueNumberOfVersions(coordinates, -1, Node.VALUE_LABEL_D3_DS1DS2DS3, 1)

        mesh = fm.findMeshByDimension(3)
        tricubichermite = eftfactory_tricubichermite(mesh, useCrossDerivatives)
        eft = tricubichermite.createEftBasic()
        elementtemplate = mesh.createElementtemplate()
        elementtemplate.setElementShapeType(Element.SHAPE_TYPE_CUBE)
        result = elementtemplate.defineField(coordinates, -1, eft)
        cache = fm.createFieldcache()
        # create nodes
        nodeIdentifier = 1
        radiansPerElementAround = 2.0 * math.pi / elementsCountAround
        wallThicknessPerElement = wallThickness / elementsCountThroughWall
        lengthPerElement = 1 / elementsCountAlong
        insideRadius = 0.25
        # scale factor of along, wall thickness, around
        scale = [lengthPerElement, wallThicknessPerElement, 0.0]

        zero = [0.0, 0.0, 0.0]
        for n3 in range(elementsCountAround):
            radian = radiansPerElementAround * n3
            for n2 in range(elementsCountThroughWall + 1):
                radius = insideRadius + wallThicknessPerElement * n2
                scale[2] = radiansPerElementAround * radius  # the arc length
                for n1 in range(elementsCountAlong + 1):

                    u = [radius * math.cos(radian), radius * math.sin(radian), n1 * lengthPerElement]
                    du_ds1_scaled = [0.0, 0.0, scale[2]]  # along
                    du_ds2_scaled = [math.cos(radian) * scale[1], math.sin(radian) * scale[1], 0.0]  # thickness
                    du_ds3_scaled = [-math.sin(radian) * scale[2], math.cos(radian) * scale[2], 0.0]  # around

                    node = nodes.createNode(nodeIdentifier, nodetemplate)
                    cache.setNode(node)
                    coordinates.setNodeParameters(cache, -1, Node.VALUE_LABEL_VALUE, 1, u)
                    coordinates.setNodeParameters(cache, -1, Node.VALUE_LABEL_D_DS1, 1, du_ds1_scaled)
                    coordinates.setNodeParameters(cache, -1, Node.VALUE_LABEL_D_DS2, 1, du_ds2_scaled)
                    coordinates.setNodeParameters(cache, -1, Node.VALUE_LABEL_D_DS3, 1, du_ds3_scaled)

                    if useCrossDerivatives:
                        coordinates.setNodeParameters(cache, -1, Node.VALUE_LABEL_D2_DS1DS2, 1, zero)
                        coordinates.setNodeParameters(cache, -1, Node.VALUE_LABEL_D2_DS1DS3, 1, zero)
                        coordinates.setNodeParameters(cache, -1, Node.VALUE_LABEL_D2_DS2DS3, 1, zero)
                        coordinates.setNodeParameters(cache, -1, Node.VALUE_LABEL_D3_DS1DS2DS3, 1, zero)
                    nodeIdentifier += 1
        # create elements
        elementIdentifier = 1
        multiplier = (elementsCountThroughWall + 1) * (elementsCountAlong + 1)
        totalNodes = (elementsCountAlong + 1) * (elementsCountThroughWall + 1) * elementsCountAround

        for e3 in range(elementsCountAround):
            for e2 in range(elementsCountThroughWall):
                for e1 in range(elementsCountAlong):
                    # element = mesh.createElement(elementIdentifier, elementtemplate)
                    n1 = 1 + e1 + (elementsCountAlong + 1) * e2 + e3 * multiplier
                    n2 = n1 + 1
                    n3, n4 = n1 + elementsCountAlong + 1, n2 + elementsCountAlong + 1
                    n5, n6 = n1 + multiplier, n2 + multiplier
                    n7, n8 = n5 + elementsCountAlong + 1, n6 + elementsCountAlong + 1
                    nodeIdentifiers = [*map(lambda value: value - totalNodes if value > totalNodes else value,
                                            [n1, n2, n3, n4, n5, n6, n7, n8])]
                    # result = element.setNodesByIdentifier(eft, nodeIdentifiers)
                    print("Element:" + str(elementIdentifier) + " Nodes: " + str(nodeIdentifiers))
                    elementIdentifier += 1
        fm.endChange()
        return []
#DOC-END create class
