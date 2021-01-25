Installation
============
1. Install git for windows (github.com/git-for-windows/git/releases)
2. Install Python (ideally 3.6.8)
  1. Navigate to downloads
  2. Download and install python 3.6.8
3. Setup Python
1.  Open command prompt
Add python to path

Install Virtualenv for your Python1.
Open command prompt
pip install virtualenv
Pip install virtualenvwrapper-win (only for windows)
Create virtual env
mkvirtualenv scaffold-venv36
To active the envronmen - In a terminal (cmd) activate the virtualenv and make sure it’s activated for the entire time you’re installing the following tools.
workon scaffold-venv36 (only windows)
source … (linux/mac)
Install OpenCMISS-ZINC:
Download the zip file from here.
Unzip the content to C/Users/upi/work/codes/python_packages/
cd to the unzipped directory.
Type pip install -e lib\python3.6\Release\opencmiss.zinc
Install PySide
Download PySide from here (Need to use this specific version for python 3 PySide‑1.2.4‑cp36‑cp36m‑win_amd64.whl).
Move to C/Users/upi/work/codes/python_packages/
 pip install PySide‑1.2.4‑cp36‑cp36m‑win_amd64.whl
Install MAPClient and its dependencies:
 cd to the python_packages
git clone https://github.com/MusculoskeletalAtlasProject/mapclient.git
pip install -e mapclient/src/.
Install a MAPClient dependency:
  pip install pmr2.wfctrl
Tools required to run ScaffoldMaker (please note that this step requires MAPClient and all the above steps installed).
Create a folder in your work directory and name it mapclient_plugins
cd  into this folder
Clone the following github projects into the mapclient_plugins folder:
https://github.com/rchristie/mapclientplugins.meshgeneratorstep.git
https://github.com/rchristie/mapclientplugins.filelocationsinkstep.git
Install scaffolder maker (https://github.com/ABI-Software/scaffoldmaker.git)
