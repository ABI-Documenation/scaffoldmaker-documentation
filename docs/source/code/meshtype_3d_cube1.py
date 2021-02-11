"""
Generates a 3-D unit Cube mesh with variable numbers of elements in 3 directions.
"""

#DOC-START imports
from __future__ import division
from opencmiss.utils.zinc.field import findOrCreateFieldCoordinates
from opencmiss.zinc.element import Element, Elementbasis
from opencmiss.zinc.field import Field
from opencmiss.zinc.node import Node
from scaffoldmaker.meshtypes.scaffold_base import Scaffold_base
from scaffoldmaker.utils.eftfactory_tricubichermite import eftfactory_tricubichermite
#DOC-END imports

#DOC-START create class cube1
class MeshType_3d_cube1(Scaffold_base):
    @staticmethod
    def getName():
        return '3D Cube 1'

    #DOC-START set-up user interface options
    @staticmethod
    def getDefaultOptions(parameterSetName='Default'):
        return {
            'size' : 1
        }

    @staticmethod
    def getOrderedOptionNames():
        return [
            'size',
        ]

    @staticmethod
    def checkOptions(options):
        if options['size'] < 1:
            options['size'] = 1

    #DOC-END set-up user interface options

    #DOC-START create mesh
    @classmethod
    def generateBaseMesh(cls, region, options):
        """
        Generate the base tricubic Hermite mesh.
        :param region: Zinc region to define model in. Must be empty.
        :param options: Dict containing options. See getDefaultOptions().
        :return: [] empty list of AnnotationGroup
        """
        # initializing classes and template
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
        # create eft
        mesh = fm.findMeshByDimension(3)
        tricubichermite = eftfactory_tricubichermite(mesh, False)
        eft = tricubichermite.createEftBasic()
        elementtemplate = mesh.createElementtemplate()
        elementtemplate.setElementShapeType(Element.SHAPE_TYPE_CUBE)
        result = elementtemplate.defineField(coordinates, -1, eft)
        # create nodes
        size = options["size"]
        nodeIdentifier = 1
        cache = fm.createFieldcache()
        dx_ds1 = [ size, 0.0, 0.0 ]
        dx_ds2 = [ 0.0, size, 0.0 ]
        dx_ds3 = [ 0.0, 0.0, size ]

        for n3 in range(2):
            for n2 in range(2):
                for n1 in range (2):
                    node = nodes.createNode(nodeIdentifier, nodetemplate)
                    cache.setNode(node)
                    x = [n1 * size, n2 * size, n3 * size]
                    coordinates.setNodeParameters(cache, -1, Node.VALUE_LABEL_VALUE, 1, x)
                    coordinates.setNodeParameters(cache, -1, Node.VALUE_LABEL_D_DS1, 1, dx_ds1)
                    coordinates.setNodeParameters(cache, -1, Node.VALUE_LABEL_D_DS2, 1, dx_ds2)
                    coordinates.setNodeParameters(cache, -1, Node.VALUE_LABEL_D_DS3, 1, dx_ds3)
                    nodeIdentifier += 1
        # create element
        elementIdentifier = 1
        element = mesh.createElement(elementIdentifier, elementtemplate)
        element.setNodesByIdentifier(eft, [1, 2, 3, 4, 5, 6, 7, 8])
        fm.endChange()
        return []
    # DOC-END create mesh

