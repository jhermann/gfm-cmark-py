gfm-cmark-py
============

 |Travis CI|  |Coveralls|  |GitHub Issues|  |License|
 |Development Status|  |Latest Version|  |Download format|  |Downloads|

A Python wrapper for GitHub's fork of ``cmark``, supporting `GFM`_
extensions. ``cmark`` is a *CommonMark* parsing and rendering library
written in C, and the project also includes Debian packaging for it.

**THIS IS IN ALPHA STATUS!**

.. contents:: **Contents**


.. _setup-start:

Introduction
------------

**TODO**

It also features *Debian* packaging for the underlying ``cmark``
library, for easy installation on distros using APT.


Usage
-----

**TODO**


Installation
------------

*gfm-cmark-py* can be installed via ``pip install gfm-cmark-py`` as usual,
see `releases <https://github.com/jhermann/gfm-cmark-py/releases>`_ for an overview of available versions.
To get a bleeding-edge version from source, use these commands::

    repo="jhermann/gfm-cmark-py"
    pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
    pip install -UI -e "git+https://github.com/$repo.git#egg=${repo#*/}"

As a developer, to create a working directory for this project, call these commands::

    git clone "https://github.com/jhermann/gfm-cmark-py.git"
    cd "gfm-cmark-py"
    command . .env --yes --develop  # add '--virtualenv /usr/bin/virtualenv' for Python2
    invoke build check

You might also need to follow some
`setup procedures <https://py-generic-project.readthedocs.io/en/latest/installing.html#quick-setup>`_
to make the necessary basic commands available on *Linux*, *Mac OS X*, and *Windows*.


Related Projects
----------------

-  `github/cmark`_ – GitHub's fork of cmark, supporting `GFM`_
   extensions.
-  `jgm/cmark`_ – *CommonMark* parsing and rendering library and program
   in C.
-  `rtfd/CommonMark-py`_ – Pure Python implementation of *CommonMark*.
-  `cmark 0.26.1-1 source package`_ (Ubuntu Zesty)


.. _GFM: https://github.github.com/gfm/
.. _github/cmark: https://github.com/github/cmark
.. _jgm/cmark: https://github.com/jgm/cmark
.. _rtfd/CommonMark-py: https://github.com/rtfd/CommonMark-py
.. _cmark 0.26.1-1 source package: https://launchpad.net/ubuntu/+source/cmark/0.26.1-1

.. |Travis CI| image:: https://api.travis-ci.org/jhermann/gfm-cmark-py.svg
    :target: https://travis-ci.org/jhermann/gfm-cmark-py
.. |Coveralls| image:: https://img.shields.io/coveralls/jhermann/gfm-cmark-py.svg
    :target: https://coveralls.io/r/jhermann/gfm-cmark-py
.. |GitHub Issues| image:: https://img.shields.io/github/issues/jhermann/gfm-cmark-py.svg
    :target: https://github.com/jhermann/gfm-cmark-py/issues
.. |License| image:: https://img.shields.io/pypi/l/gfm-cmark-py.svg
    :target: https://github.com/jhermann/gfm-cmark-py/blob/master/LICENSE
.. |Development Status| image:: https://pypip.in/status/gfm-cmark-py/badge.svg
    :target: https://pypi.python.org/pypi/gfm-cmark-py/
.. |Latest Version| image:: https://img.shields.io/pypi/v/gfm-cmark-py.svg
    :target: https://pypi.python.org/pypi/gfm-cmark-py/
.. |Download format| image:: https://pypip.in/format/gfm-cmark-py/badge.svg
    :target: https://pypi.python.org/pypi/gfm-cmark-py/
.. |Downloads| image:: https://img.shields.io/pypi/dw/gfm-cmark-py.svg
    :target: https://pypi.python.org/pypi/gfm-cmark-py/
