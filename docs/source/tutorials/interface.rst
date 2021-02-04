*****************************************************
Interface : How to create a scaffold maker workflow ?
*****************************************************

.. toctree::
   :maxdepth: 2

========
Workflow
========

Plugins
--------

Open mapclient window and bring the mesh generator plugin into the workspace. The mesh generator plugin saves the mesh
in your folder. Do the same with file location sink plugin.
Then, connect the output port of mesh generator plugin to the input port of file location sink plugin.

.. image:: C:\Users\maria\Desktop\NZ\mapclient.png
  :width: 400

Whenever you bring a plugin into the mapclient window, there is a tiny button on the bottom right that is usually red;
That means that the plugin is not configured, by clicking on the red button, you will have a configuration step that is
different for each plugin.

* For the mesh generator configuration, click on the red button on the bottom right of the plugin and give it a name in
the identifier field (for example Scaffold). Click ok, the button on the bottom right should be green now.
* For the file location sink configuration, click on the red button on the bottom right of the plugin and configure it.
For this plugin, give it a name in the identifier field (e.g. output) and add a file location. In the file field, click
on the three dots, in the work directory create a folder call scaffold_sink for example and select it. Click ok, the
button on the bottom right should be green now.

Workspace
---------

Now, save the workspace. Click on File, then Save As. In the save popup, create a new folder called ‘mapclient_workflows’
inside work/codes. Open the folder created and create a new folder to contain your new workflow name in this example
“example-workflow-scaffold”. Select ok.

Then run your workflow and click on Execute on the bottom right of mapclient window. It will open a new window. When the
window opens, an easy case appears for example a cube.

If you need, to rerun a workflow that has already been saved, open the command prompt, mapclient should be run with the
~w flag. E.g.
mapclient -w C:\Users\upi\codes\mapclient_workflows\example-workflow-scaffold\

=============
Control panel
=============

Visualisation part
------------------

In the bottom part of the control panel, there is a display tab and an annotation tab. At this stage, focus on the
display tab. The annotation tab  is more useful for a complicated scaffold.
In the display tab, there are many options. In this case with the cube, you can currently see a cube which has lines,
transparent surfaces... Select what you want to add on your cube and it will appear, it is really intuitive.
In the case of the derivatives, there are two options:

* Click once on it, in the case selected, there is a small square. In this case, only the derivative of the node that
you want will appear. To select it, hold S on your keyboard and click on the once you want.

.. image:: C:\Users\maria\Desktop\NZ\derivative-square.png
  :width: 400

* Click again on it, in the case selected, there is a small cross. In this case, all the derivatives of the nodes will
appear.

.. image:: C:\Users\maria\Desktop\NZ\derivatives-square.png
  :width: 400

You can also change the display of the different derivatives. This is a cube elements so obviously, it has three local
directions so the derivatives you will expect, are derivatives of the coordinates x, y, z.

Parameters of the scaffold
--------------------------

* Mesh time:

We are looking at the mesh time which is a 3D Box 1. So, the mesh time whenever you create a scaffold, the name in
convention goes with the dimension of the scaffold; so, if you are working with a cubic hermite or bicubic linear
hermite, it is a volume mesh, so you always put 3D. Then you put the name of the scaffold (here Box) and the number
of the version (here 1). Sometimes you have multiple versions of the scaffold and then you have for example 3D Box2,
3D Box 3, etc.

* Number of elements:

Then there is the parameter sets. In a study where you are creating a scaffold, let’s say you are creating a pectoral
muscle for human, or if it is different for male and female or if you are creating a pectoral muscle for rats or for
different species, you may have a different parameter set that you can select. I will show you this when we work with
different organs scaffold because with a box you can only have one shape. These parameters can be change in different
directions or number of elements.
These directions are set depending how you want to call it. For example, on the cube they are called 1,2 and 3.
And we named them assuming they come from the direction of the derivatives.

* Refine:

Usually for every scaffold, we have a refined option. This option refines your element into a linear mesh to export it
as a VTK or something else. After using this option, there is not any derivative left because our element is now linear.
Then you can refine in different directions to get a refined mesh.
Then, we have two new buttons that you may not have: smooth derivative and print nodes parameters. You may have to update
to a scaffold maker.

* Print nodes parameters:

If you click on Print nodes parameters, you can change the format which will print out the matrix of value in your
terminal or in your Python IDE. These values represent the coordinates of your scaffold. Because our system is linear,
the derivative along x is only changing the x value, it is the same for y and z.

* Smooth derivative:

If you are working on a scaffold and you want to change the derivative a little bit and you want to save that mesh, you
can pull down S key, select a node and change the derivative in some direction. After changing derivatives directions
and node place, you can smooth it with the second button.
There are other options to smooth the derivatives: the arithmetic scaling mode and the harmonic one. Moreover, if you
click on update the direction, the software will change the direction to find the better option.

* Delete element 1D ranges:

You can delete any element ranges. You can make appear the number of each element. After deciding the ones, you want to
delete, you just have to write them separated by a coma (,) or by a dash (-) if they follow each other. To restore them
you just must erase them.

* Rotation, scale and translation:

You can rotate, scale and translate the scaffold by changing values. You can also do this by pulling down the A key and
with the left button on the mouse, you can rotate and translate and with the right button and holding on A key, you can
change the scale. The A key allow to impact the scaffold while without pulling down this button, only the camera moves,
not the element. After moving the scaffold where you wanted it, you need to click on apply transformation to save the
changes.
