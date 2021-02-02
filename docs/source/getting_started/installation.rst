*******
Procedure
*******

.. toctree::
   :maxdepth: 2

=======
Softwares
=======

Git
-------------------------------------------

First, install git for Windows (follow this `link
<https://github.com/git-for-windows/git/releases/>`_ to download it).


Python
-------------------------------------------

Assuming you don't have Python already, install it ideally with the version 3.6.8.

* Download the `executable installer x86-64 <https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe>`_
* Open on Window the command prompt
* Add python to path

Virtual environment
-------------------------------------------

To install a virtual environment for your Python, follow the next steps:

* Open the command prompt, and execute it:

```bash
pip install virtualenv
```

* If you are working on Windows, execute in the command prompt the next step:

```bash
pip install virtualenvwrapper-win (only for windows)
```

* Now, create the virtual environment:

```bash
mkvirtualenv scaffold-venv36
```

* Then, activate the virtual environment and make sure it is still activate for the entire time
you are installing the following tools. Two possibilities:

      *  If you are working on Windows, execute in the command prompt the next step:

```bash
workon scaffold-venv36
```
      *  If you are working on Linux or Mac, execute in the command prompt the next step and complete it:
```bash
source [folder]/activate
```

OpenCMISS-ZINC
-------------------------------------------

Your virtual environment is still activate, download the `zip file <http://opencmiss.org/downloads.html#/>`_
Click on Get OpenCMISS Librairies and download it. Unzip the content to C/Users/upi/work/codes/python_packages/.
Then in the command prompt, change the directory:

```bash
cd C/Users/upi/work/codes/python_packages/
pip install -e lib\python3.6\Release\opencmiss.zinc
```

PySide
-------------------------------------------

Download `PySide <https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyside>`_ and be careful to select this specific version
for python 3 PySide‑1.2.4‑cp36‑cp36m‑win_amd64.whl). Then, return to the command prompt and enter the following steps:

```bash
cd C/Users/upi/work/codes/python_packages/
pip install PySide‑1.2.4‑cp36‑cp36m‑win_amd64.whl
```

MAPClient
-------------------------------------------

Install MAPClient and its dependencies by writing the next instructions in the command prompt:

```bash:
cd C/Users/upi/work/codes/python_packages/
git clone https://github.com/MusculoskeletalAtlasProject/mapclient.git
pip install -e mapclient/src/
```

Then, install a MAPClient dependency:

```bash
pip install pmr2.wfctrl
```

These tools are required to run ScaffoldMaker so please note that this step requires MAPClient and all the above steps
installed earlier. Create a folder in your work directory and name it mapclient_plugins. Then, change into this folder
in the command prompt.
Clone the following github projects into the mapclient_plugins folder:

```bash
git clone https://github.com/rchristie/mapclientplugins.meshgeneratorstep.git
git clone https://github.com/rchristie/mapclientplugins.filelocationsinkstep.git
```

Install `scaffolder maker <https://github.com/ABI-Software/scaffoldmaker.git>`_ and change to the python_packages into
the command prompt. Then, clone the opencmiss plugin:

```bash
https://github.com/OpenCMISS-Bindings/opencmiss.utils.git
```

Change into opencmiss.utils folder and open setup.py. Look for the line “requires = [‘opencmiss.zinc’]” and replace with
“requires = []”. Then , in the command prompt, write:

```bash
pip install -e .
```

Change to the python_packages and clone zingwidgets plugins:

```bash
git clone https://github.com/OpenCMISS-Bindings/opencmiss.zincwidgets.git
```

Change into opencmiss.zincwidgets folder and open setup.py. Look for the line requires = ['opencmiss.utils >= 0.2.0',
'PySide2', 'opencmiss.zinc']” and replace with  “requires = []”. Then , in the command prompt, write:

```bash
pip install -e .
```

Scaffoldmaker
-------------------------------------------

To install scaffoldmaker, change to the python_packages folder.

* For developers: Fork the repository

```bash
git clone https://github.com/your_github_username/scaffoldmaker.git
```

* For users:

```bash
git clone https://github.com/ABI-Software/scaffoldmaker.git
```

Change into scaffoldmaker folder and add in the command prompt:

```bash
pip install -e .
```

To install Scaffodfitter, go to to the python_packages folder in the command prompt:

```bash
git clone https://github.com/ABI-Software/scaffoldfitter.git
```

Change to scaffoldfitter folder and write :

```bash
pip install -e .
```

To install geometric fit step mapclient plugin, change into mapclient_plugins folder.

```bash
git clone https://github.com/ABI-Software/mapclientplugins.geometricfitstep.git
```

Loading plugins into mapclient
-------------------------------------------

Check for the virtual environment if it is not already activated, do it and then, open mapclient.
Go to Tools, then Plugin Manager, Add Directory,  add work/codes/mapclient_plugins/, click select folder and click
reload, press ok. Exit mapclient. Run mapmapclient again. The new plugins should be visible as Geometric fit,
File location Sink and Mesh generator.

=======
Test
=======


Test if OpenCMISS-ZINC is installed successfully. In a terminal with the virtualenv activated, type the following steps:

```bash
python
from opencmiss.zinc.context import Context
```
If no errors show up, then everything looks good!
Now, check if MAPClient is installed successfully. In a terminal with the virtualenv activated, type the following step:

```bash
.mapclient
```

If no errors show up the MAPClient window pops up, then everything looks good!


