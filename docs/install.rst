======================
Install and Contribute
======================

This page containst the lists of dependencies and install instructions for two scenarios. Firstly, "General use" for anyone who just whishes to use the algorithms. Secondly, instruction on how to install the package in order to be able to build the docs and run tests.

General Use
===========

This section contains the dependencies and install instructions for regular usage of the sklvq package. If you wish to contribute to the package please see the `Contribute`_ section.

Dependencies
------------

The sklvq toolbox requires the following packages to be installed:

* numpy
* scipy
* scikit-learn

Installation
------------
Sklvq can be installed using pip::

    pip install sklvq

Another option is to clone the repository and run the setup.py file. The following (terminal/cmd) commands can be used to clone the repository and install sklvq with all dependencies::

    git clone https://github.com/rickvanveen/sklvq.git
    cd sklvq
    pip install .

Or install using pip from GitHub directly::

    pip install -U git+https://github.com/rickvanveen/sklvq.git

Contribute
==========

You can contribute to this code through pull requests on GitHub. Please, make sure that your code is coming with unit tests to ensure full coverage and continuous integration in the API. Follow the instruction below in order to install all necessary dependencies for development.

Dependencies
------------

In addition to the regular dependencies, sklvq requires a number of packages for testing and building the documentation:

Testing:
    * pytest
    * pytest-cov

Documentation:
    * sphinx
    * sphinx-gallery
    * sphinx_rtd_theme
    * numpydoc
    * matplotlib

Installation
------------

The package can be cloned using the following commands::

    git clone https://github.com/rickvanveen/sklvq.git
    cd sklvq

Using the following addition to the `pip` command, one can install the dependencies automatically::

    pip install .[tests]

or in order to be able to build the documentation::

    pip install .[docs]

or simply by passing them at the same time (note the lack of whitespace)::

    pip install .[tests,docs]


Running Tests
-------------

Every module contains its own test folder. Where every file is prepended with `test_`. The tests
can be run by using the following command when in the sklvq module folder::

    pytest .

Building Docs
-------------

The html docs can be build using the following command (in the docs folder)::

    make html

This will generate a build folder from which the index.html can be opened locally. Other options
are also available see the 'Makefile' in the doc folder.
