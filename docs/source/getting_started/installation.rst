*********
Installation
*********

.. toctree::
    :maxdepth: 2
    :caption: Contents:
=========
Procedure
=========

Git
---

First, install git for Windows (follow this `link <https://github.com/git-for-windows/git/releases/>`_ to download it).

Python
------

Assuming you don't have Python already, install it ideally with the version 3.6.8.

* Download the `executable installer x86-64 <https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe>`_
* Open on Window the command prompt
* Add python to path

Virtual environment
-------------------

To install a virtual environment for your Python, follow the next steps:

* Open the command prompt, and execute it:

.. code-block:: bash
    pip install virtualenv

* If you are working on Windows, execute in the command prompt the next step:

.. code-block:: bash
    pip install virtualenvwrapper-win (only for windows)

* Now, create the virtual environment:

.. code-block:: bash
    mkvirtualenv scaffold-venv36

* Then, activate the virtual environment and make sure it is still activate for the entire time
you are installing the following tools. Two possibilities:

      *  If you are working on Windows, execute in the command prompt the next step:

.. code-block:: bash
    workon scaffold-venv36

      *  If you are working on Linux or Mac, execute in the command prompt the next step and complete it:

.. code-block:: bash
    source [folder]/activate

OpenCMISS-ZINC
--------------

Your virtual environment is still activate, download the `zip file <http://opencmiss.org/downloads.html#/>`_
Click on Get OpenCMISS Librairies and download it. Unzip the content to C/Users/upi/work/codes/python_packages/.
Then in the command prompt, change the directory:

.. code-block:: bash
    cd C/Users/upi/work/codes/python_packages/
    pip install -e lib\python3.6\Release\opencmiss.zinc

PySide
------

Download `PySide <https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyside>`_ and be careful to select this specific version
for python 3 PySide‑1.2.4‑cp36‑cp36m‑win_amd64.whl). Then, return to the command prompt and enter the following steps:

.. code-block:: bash
    cd C/Users/upi/work/codes/python_packages/
    pip install PySide‑1.2.4‑cp36‑cp36m‑win_amd64.whl

MAPClient
---------

Install MAPClient and its dependencies by writing the next instructions in the command prompt:

.. code-block:: bash
    cd C/Users/upi/work/codes/python_packages/
    git clone https://github.com/MusculoskeletalAtlasProject/mapclient.git
    pip install -e mapclient/src/

Then, install a MAPClient dependency:

.. code-block:: bash
    pip install pmr2.wfctrl

These tools are required to run ScaffoldMaker so please note that this step requires MAPClient and all the above steps
installed earlier. Create a folder in your work directory and name it mapclient_plugins. Then, change into this folder
in the command prompt.
Clone the following github projects into the mapclient_plugins folder:

.. code-block:: bash
    git clone https://github.com/rchristie/mapclientplugins.meshgeneratorstep.git
    git clone https://github.com/rchristie/mapclientplugins.filelocationsinkstep.git

Install `scaffolder maker <https://github.com/ABI-Software/scaffoldmaker.git>`_ and change to the python_packages into
the command prompt. Then, clone the opencmiss plugin:

.. code-block:: bash
    https://github.com/OpenCMISS-Bindings/opencmiss.utils.git

Change into opencmiss.utils folder and open setup.py. Look for the line “requires = [‘opencmiss.zinc’]” and replace with
“requires = []”. Then , in the command prompt, write:

.. code-block:: bash
    pip install -e .

Change to the python_packages and clone zingwidgets plugins:

.. code-block:: bash
    git clone https://github.com/OpenCMISS-Bindings/opencmiss.zincwidgets.git

Change into opencmiss.zincwidgets folder and open setup.py. Look for the line requires = ['opencmiss.utils >= 0.2.0',
'PySide2', 'opencmiss.zinc']” and replace with  “requires = []”. Then , in the command prompt, write:

.. code-block:: bash
    pip install -e .

Scaffoldmaker
-------------

To install scaffoldmaker, change to the python_packages folder.

* For developers: Fork the repository

.. code-block:: bash
    git clone https://github.com/your_github_username/scaffoldmaker.git

* For users:

.. code-block:: bash
    git clone https://github.com/ABI-Software/scaffoldmaker.git

Change into scaffoldmaker folder and add in the command prompt:

.. code-block:: bash
    pip install -e .

To install Scaffoldfitter, go to to the python_packages folder in the command prompt:

.. code-block:: bash
    git clone https://github.com/ABI-Software/scaffoldfitter.git

Change to scaffoldfitter folder and write :

.. code-block:: bash
    pip install -e .

To install geometric fit step mapclient plugin, change into mapclient_plugins folder.

.. code-block:: bash
    git clone https://github.com/ABI-Software/mapclientplugins.geometricfitstep.git

Loading plugins into mapclient
------------------------------

Check for the virtual environment if it is not already activated, do it and then, open mapclient.
Go to Tools, then Plugin Manager, Add Directory,  add work/codes/mapclient_plugins/, click select folder and click
reload, press ok. Exit mapclient. Run mapmapclient again. The new plugins should be visible as Geometric fit,
File location Sink and Mesh generator.

=======
Docker
=======

Click on the link below to know how to install it. This software can help you if the bottom procedure doesn't
work. In some cases, the virtual environment or python are enabled to work so you can try this software to have a
mapclient available.

`How to install Docker? <https://opencmiss-iron-tutorials.readthedocs.io/en/latest/getting_started/installation/docker.html>`_

When Docker is installed, you can try to use Pycharm by following this other `documentation <https://opencmiss-iron-tutorials.readthedocs.io/en/latest/getting_started/running/pycharm.html#windows>`_
Be careful, even after following all these steps, Docker can't be run. One solution could be to check the number of
XLaunch launch on your computer and to change by the right value.

.. code-block:: bash
    $env:DISPLAY= 'localhost:0.0'
    docker run `
        --rm `
        --env DISPLAY=${env:IPAddress}:0.0 `
        --name opencmiss-iron `
        -it `
        --sysctl net.ipv6.conf.all.disable_ipv6=0 `
        -v c/Users/${env:UserName}/Documents/oc/opt:/home/jovyan/work `
        -v c/Users/${env:UserName}/Documents/oc/usr/local:/home/jovyan/.local `
        -v c/Users/${env:UserName}/Documents/oc/usr/cache:/home/jovyan/.cache `
        -v c/Users/${env:UserName}/Documents/oc/usr/etc/jupyter:/etc/jupyter `
        -v c/Users/${env:UserName}/Documents/oc/usr/bin/:/usr/local/bin/ `
        -v c/Users/${env:UserName}/Documents/oc/usr/config:/home/jovyan/.config `
        -v c/Users/${env:UserName}/Documents/oc/usr/java:/home/jovyan/.java `
        -v c/Users/${env:UserName}/Documents/oc/usr/PyCharm:/home/jovyan/.PyCharm `
        prasadbabarendagamage/opencmiss-iron:1.0-minimal-ssh start-pycharm.sh


