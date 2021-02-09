.. _tube:

Creating a 3D tube
====================

.. role:: pyth(code)
  :language: python

Once you have create a :ref:`single-element cube <cube>`, let's try to make a 3D tube with more than 1 element.

Set-up files and modules
-------------------------
Create a file and name it :file:`meshtype_3d_tube2.py` in
the :file:`.\\src\\scaffoldmaker\\meshtypes` folder. Remember to load it in :file:`.\\src\\scaffoldmaker\\scaffolds.py`. Then :pyth:`import` the following
modules which help us to create field, nodes, elements and interpolation functions.

.. literalinclude:: ../../code/meshtype_3d_tube2.py
   :language: python
   :linenos:
   :start-after: #DOC-START imports
   :end-before: #DOC-END imports

Creating user interface options
-------------------------------

As mentioned, this time we will let the user decide the number of elements in each direction.
Therefore we should set-up the user interface options as followed:

.. literalinclude:: ../../code/meshtype_3d_tube2.py
   :language: python
   :linenos:
   :start-after: #DOC-START create class
   :end-before: # generate mesh

Everything is pretty similar to what we have done in the :ref:`3D cube <cube>` tutorial. Feel free to add your own options or constraints.

Creating the mesh
----------------------

Before locating each nodes, we have to initialize the following objects and classes:

* All the options values
* Mathematical field
* Coordinates
* Nodes class and node templates
* Mesh
* Interpolation function, element template, and element field template.
* cache

.. literalinclude:: ../../code/meshtype_3d_tube2.py
   :language: python
   :linenos:
   :start-after: # generate mesh
   :end-before: # create nodes

For each node, we want to calculate its global coordinates :math:`u`, and its derivatives with respect to the local coordinates
:math:`\frac{du}{d\zeta}|_1, \frac{du}{d\zeta}|_2, \frac{du}{d\zeta}|_3`. Here is an example:

.. literalinclude:: ../../code/meshtype_3d_tube2.py
   :language: python
   :linenos:
   :start-after: # create nodes
   :end-before: # create elements

Here, we define that :math:`\zeta_1, \zeta_2, \zeta_3` are the element parameters along the tube, through the wall, and around the tube respectively. We can find the derivatives by multiplying the arc-length
based derivatives and the corresponding scale factor. In this case, we set all cross derivatives to zero.

With all nodal values set, we need to construct elements. Unlike the 3D cube example, where we only
have 1 element, arranging node identifiers in this case can be a little bit tricky.

.. literalinclude:: ../../code/meshtype_3d_tube2.py
   :language: python
   :linenos:
   :start-after: # create elements
   :end-before: #DOC-END create class

If you look back, our node identifiers accumulate in the following order:

* along the tube :pyth:`e1`
* through the wall :pyth:`e2`
* around the tube :pyth:`e3`

We can address the first node identifier in each element, then use the first node identifier to locate others. In the
last iteration of :pyth:`e3`, nodes should return to the starting position. Thus we subtracted :pyth:`totalNodes`
from each node identifier if it exceeds the total number of nodes, to complete the loop. If you are struggling
to picture this, see the figure below for more information.

.. image:: ../../images/creating_meshtype/tube.png
    :class: with-shadow

And each element should include these nodes:

::

    Element:1 Nodes: [1, 2, 4, 5, 7, 8, 10, 11]
    Element:2 Nodes: [2, 3, 5, 6, 8, 9, 11, 12]
    Element:3 Nodes: [7, 8, 10, 11, 13, 14, 16, 17]
    Element:4 Nodes: [8, 9, 11, 12, 14, 15, 17, 18]
    Element:5 Nodes: [13, 14, 16, 17, 19, 20, 22, 23]
    Element:6 Nodes: [14, 15, 17, 18, 20, 21, 23, 24]
    Element:7 Nodes: [19, 20, 22, 23, 1, 2, 4, 5]
    Element:8 Nodes: [20, 21, 23, 24, 2, 3, 5, 6]

Of course this is just one way of doing it. You can always find a way that is more intuitive to you. Be creative.