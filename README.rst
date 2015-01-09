ModbusLibrary for Robot Framework
=================================

Introduction
------------

ModbusLibrary is a `Robot Framework <http://robotframework.org>`__ test
library for testing Modbus.

The library has the following main usages:

- Executing commands on the remote machine, either with blocking or
  non-blocking behavior.
- Writing and reading in an interactive shell.
- Transferring files and directories over SFTP.
- Ensuring that files and directories exist on the remote machine.

SSHLibrary is open source software licensed under `Apache License 2.0
<http://www.apache.org/licenses/LICENSE-2.0.html>`__.

Installation
------------

When installing ModbusLibrary on UNIX-like machines with Python, the easiest
approach is using `pip <http://pip-installer.org>`__::

    pip install robotframework-modbuslibrary

Alternatively you can download the source distribution from `PyPI
<https://pypi.python.org/pypi/robotframework-modbuslibrary>`__, extract
it, and install it::

    python setup.py install

For more detailed installation instructions see `INSTALL.rst`__.

.. Using full URL here to make it work also on PyPI
__ https://github.com/robotframework/SSHLibrary/blob/master/INSTALL.rst

Documentation
-------------

Keyword documentation by version can be found from
http://robotframework.org/SSHLibrary/.

For general information about using test libraries with Robot Framework, see
`Robot Framework User Guide`__.

__ http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#using-test-libraries
