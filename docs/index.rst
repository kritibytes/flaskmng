.. flaskmng documentation master file, created by
   sphinx-quickstart on Wed Apr 14 19:38:13 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to flaskmng's documentation!
====================================

`Github repository <https://github.com/kritibytes/flaskmng>`_

What is flaskmng?
#################

**flaskmng** is a tool that manages Flask project. It is designed in MVT architecture.

Usage
#####

First of all, you must create virtual environment.

.. code:: bash

   > python -m venv env

To activate,

.. code:: bash

   > . env/Scripts/activate # for Windows
   > source env/bin/activate # for Linux

Then, for installing flaskmng to the virtual environment you must use
pip. After installing pip enter the command given below:

.. code:: bash

   > pip install flaskmng

Command Line Interface
######################

.. click:: flaskmng.__main__:main
   :prog: flaskmng
   :nested: full
   :commands: startproject,startapp,removeapp

Conclusion
##########

In conclusion, your flask project ready to development. Enjoy the
advantages of **flaskmng**.

**Thanks for using!**
---------------------

