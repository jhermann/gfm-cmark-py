#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, invalid-name, wrong-import-position
"""
    gfm-cmark-py - A Python wrapper for GitHub's fork of 'cmark', supporting GFM) extensions.

    This setuptools script follows the DRY principle and tries to
    minimize repetition of project metadata by loading it from other
    places (like the script module's ``__*__`` attributes). Incidently,
    this makes the script almost identical between different projects.

    It is also importable (by using the usual ``if __name__ == '__main__'``
    idiom), and exposes the project's setup data in a ``project`` dict.
    This allows other tools to exploit the data assembling code contained
    in here, and again supports the DRY principle. The ``rituals`` package
    uses that to provide Invoke tasks that work for any project, based on
    its project metadata.

    Copyright ©  2017 Jürgen Hermann <jh@web.de>
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this
      list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.

    * Neither the name of the copyright holder nor the names of its
      contributors may be used to endorse or promote products derived from
      this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

project = dict(
    name='gfm-cmark-py',
    url='https://github.com/jhermann/gfm-cmark-py',
    license="BSD 3-clause",
    keywords='hosted.by.github cmark markdown markup gfm ctypes wrapper',
    py_modules=['gfm_cmark'],

    install_requires=[],

    entry_points={
        "console_scripts": [
            "gfm-cmark = gfm_cmark:run",
        ],
    },

    # Added by the code below:
    #   version author author_email (from script module)
    #   description (from doc string above)
    #   long_description (from README)
    #   classifiers (see below)
)

classifiers = """
# Details at http://pypi.python.org/pypi?:action=list_classifiers
Development Status :: 3 - Alpha
#Development Status :: 4 - Beta
#Development Status :: 5 - Production/Stable
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Environment :: Console
Intended Audience :: Developers
Intended Audience :: Information Technology
Intended Audience :: System Administrators
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Topic :: Utilities
"""


# Beyond this point, code is not project-specific
import io
import os
import re
import sys
import json

try:
    from setuptools import setup
except ImportError as exc:
    raise RuntimeError("Cannot install '{0}', setuptools is missing ({1})"
                       .format(project['name'], exc))

project_root = os.path.abspath(os.path.dirname(__file__))
script_name = os.path.join(project_root, project['py_modules'][0] + '.py')
expected_keys = "version author author_email".split()
with io.open(script_name, encoding='utf-8') as handle:
    for line in handle:
        match = re.match(r"""^__({})__ += (?P<q>['"])(.+?)(?P=q)$"""
                         .format('|'.join(expected_keys)), line)
        if match:
            project[match.group(1)] = match.group(3)

project.update(dict(
    description=__doc__.split('.')[0].split(' - ', 1)[1].strip(),
    long_description=(io.open('README.rst', encoding='UTF-8').read()
                      .split('\n.. _setup-start:', 1)[-1].strip()),
    classifiers=[i.strip()
                 for i in classifiers.splitlines()
                 if i.strip() and not i.strip().startswith('#')],
    keywords=project['keywords'].replace(',', ' ').strip().split(),
))

# Ensure 'setup.py' is importable by other tools, to access the project's metadata
__all__ = ['project', 'project_root']
if __name__ == '__main__':
    if '--metadata' in sys.argv[:2]:
        json.dump(project, sys.stdout, default=repr, indent=4, sort_keys=True)
        sys.stdout.write('\n')
    else:
        setup(**project)
