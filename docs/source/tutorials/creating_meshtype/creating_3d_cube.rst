.. _cube:

Creating a 3D cube
========================

.. role:: pyth(code)
  :language: python

Let's create a 3D cube as your first mesh type.

Set-up files and modules
-------------------------

First, navigate to where you installed scaffoldmaker, find the :file:`.\\src\\scaffoldmaker\\meshtypes` folder. This is where you put all mesh types.
Create a mesh type file,
e.g., :file:`meshtype_3d_cube1.py`.

In the ``python`` file you just created, load the following modules.

.. literalinclude:: ../../code/meshtype_3d_cube1.py
   :language: python
   :linenos:
   :start-after: #DOC-START imports
   :end-before: #DOC-END imports

Add a new :pyth:`class`, which will contain all the information related to the mesh type.

.. literalinclude:: ../../code/meshtype_3d_cube1.py
   :language: python
   :linenos:
   :start-after: #DOC-START create class cube1
   :end-before: #DOC-START set-up user interface options

.. Note::
    It's a good practice to name your mesh type file and :pyth:`class` following this particular syntax.

We have to let ``scaffold`` know that we have created a new mesh type. Open :file:`.\\src\\scaffoldmaker\\scaffolds.py`,
and :pyth:`import` the mesh type.

.. code-block:: python
    :emphasize-lines: 2

    ...
    from scaffoldmaker.meshtypes.meshtype_3d_cube1 import MeshType_3d_cube1
    ...

We also have to add the imported class into the initializing list of :pyth:`class Scaffolds()`.

.. code-block:: python
    :emphasize-lines: 5

    class Scaffolds(object):
        def __init__(self):
            self._allScaffoldTypes = [
                ...
                MeshType_3d_cube1,
                ...

.. Note::
     When importing and initializing, you should put your mesh type in the correct alphabetical order.


Set-up user interface options
------------------------------

The next step is to set-up an user interface so you can have more control over the object. In practice, we want to add options to control the
number of elements. For the purpose of demonstration, our cube mesh will have only 1 element as we want to make everything as simple as possible.

Now, go back to :file:`meshtype_2d_cube1.py`. Under :pyth:`class MeshType_3d_cube1()`, add the following lines to modify the size of the square cube.

.. literalinclude:: ../../code/meshtype_3d_cube1.py
   :language: python
   :linenos:
   :start-after: #DOC-START create class cube1
   :end-before: #DOC-END set-up user interface options

+------------------------------------+---------------------------------------------------------------------+
| Methods                            | description                                                         |
+====================================+=====================================================================+
| :pyth:`.getDefaultOptions()`       | Initialize options and set default values.                          |
+------------------------------------+---------------------------------------------------------------------+
| :pyth:`.getOrderedOptionNames()`   | Define the order of options displayed on screen.                    |
+------------------------------------+---------------------------------------------------------------------+
| :pyth:`.checkOptions()`            | Set restrictions for the input. E.g., minimum value.                |
+------------------------------------+---------------------------------------------------------------------+

Creating the mesh
------------------

Finally we can start to design the mesh. This is where you write most of your code. Include the following code in the :pyth:`MeshType_3d_cube` class:

.. literalinclude:: ../../code/meshtype_3d_cube1.py
    :language: python
    :linenos:
    :start-after: #DOC-START create mesh
    :end-before:  # create eft

Here, :pyth:`fm` handles everything in the mathematical field (mesh, nodeset, etc). Construct the coordinates system using :pyth:`.findOrCreateFieldCoordinates()`.
We then use :pyth:`.findNodesetByFieldDomainType()` to create nodes class, and use :pyth:`.createNodetemplate()` to create a node template for all nodes.
As we want to create a cube using tri-cubic hermite interpolation, we have to set-up the node template such that every node can store its global coordinates
and the derivative of the global coordinate with respect to the local element coordinate. Therefore we call the :pyth:`.setValueNumberOfVersions()` 4 times, each one with a
unique label to pre-define what parameters we are going to store in a node. For more details of :pyth:`Field` class, check `OpenCMISS-Zinc documentation <http://opencmiss.org/zinc/latest/classes.html>`_.

.. literalinclude:: ../../code/meshtype_3d_cube1.py
    :language: python
    :start-after: # create eft
    :end-before: # create nodes
    :linenos:

Continuing from above, we then initialize the mesh and define our interpolation function
using :pyth:`.findMeshByDimension()` and :pyth:`eftfactory_tricubichermite()` respectively. :pyth:`eft` refers to element field template, a template that defines
field parameter mapping and interpolation over an element. If you want to use an interpolation function that is not included in :ref:`utils`,
you may have to manually set-up eft using basic functions provided by `Zinc <http://opencmiss.org/zinc/latest/classes.html>`_.

Just like nodes, we also have to create a template for elements using :pyth:`.createElementtemplate()`.
:pyth:`.setElementShapeType()` defines
the structure of each element. At last, we use :pyth:`defineField` to define the field components
on the element template using the element field template. For more details, check `Zinc element template
<http://opencmiss.org/documentation/apidoc/zinc/latest/classOpenCMISS_1_1Zinc_1_1Elementtemplate.html>`_.

Now we just have to add coordinates and derivatives to each nodes.

.. literalinclude:: ../../code/meshtype_3d_cube1.py
    :language: python
    :start-after: # create nodes
    :end-before: # create element
    :linenos:

We create each node by calling the :pyth:`.createNode()` method with our already defined node template.
Note that each node must have an unique identifier which is important for creating elements in the next step.
We also have to create :pyth:`cache` as a temporary reference before
assigning parameters to each node with :pyth:`.setNodeParameters()` method.

We are almost there. Now, let's create the element which contains all our nodes. As there is only 1 element, the task is simple.

.. literalinclude:: ../../code/meshtype_3d_cube1.py
    :language: python
    :start-after: # create element
    :end-before: # DOC-END create mesh
    :linenos:

Be careful, the order of node identifier matters. For example, between node 1 and 2, we use the derivatives of the global
coordinates with respect to the local coordinates in the first direction, e.g. :pyth:`dx_ds1`. Whereas :pyth:`dx_ds2`
generates mesh in the second direction, i.e, along node 1 and node 3. :pyth:`dx_ds3` is the derivatives corresponding to the third
direction, i.e. along node 1 and node 5. We will look at this in more details in the :ref:`next tutorial <tube>`.

At last, call :pyth:`fm.endChange()` to finish the task.
