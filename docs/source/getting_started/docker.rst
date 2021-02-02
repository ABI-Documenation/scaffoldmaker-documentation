Docker
===========

.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_

Click on the links in the headings to know how to install it. This software can help you if the procedure doesn't work.
In some cases, the virtual environment or python are enabled to work so you can try this software to have a mapclient
available.

`How to install Docker? <https://opencmiss-iron-tutorials.readthedocs.io/en/latest/getting_started/installation/docker.html>`_

When Docker is installed, you can try to use Pycharm by following this other `documentation <https://opencmiss-iron-tutorials.readthedocs.io/en/latest/getting_started/running/pycharm.html#windows>`_
Be careful, even after following all these steps, Docker can't be run. One solution could be to check the number of
XLaunch launch on your computer and to change by the right value.

```bash
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
```
