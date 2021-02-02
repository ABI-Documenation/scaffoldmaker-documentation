*******
Tutorial : How to create a scaffold maker workflow ?
*******

.. toctree::
   :maxdepth: 2

=======
Workflow
=======

Plugins
-------------------------------------------

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
-------------------------------------------

Now, save the workspace. Click on File, then Save As. In the save popup, create a new folder called ‘mapclient_workflows’
inside work/codes. Open the folder created and create a new folder to contain your new workflow name in this example
“example-workflow-scaffold”. Select ok.

Then run your workflow and click on Execute on the bottom right of mapclient window. It will open a new window. When the
window opens, an easy case appears for example a cube.

If you need, to rerun a workflow that has already been saved, open the command prompt, mapclient should be run with the
~w flag. E.g.
mapclient -w C:\Users\upi\codes\mapclient_workflows\example-workflow-scaffold\

=======
Control panel
=======

Visualisation part
-------------------------------------------

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
-------------------------------------------

