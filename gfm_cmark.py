# -*- coding: utf-8 -*-
"""
    gfm-cmark-py – A Python wrapper for GitHub's fork of 'cmark', supporting GFM) extensions.

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
from __future__ import absolute_import, unicode_literals, print_function

import sys
import time
import errno
import codecs
import logging
import argparse

__version__ = '0.1.0'
__author__ = 'Jürgen Hermann'
__author_email__ = 'jh@web.de'


def setup():
    """Set up runtime environment."""
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf8')(sys.stderr)
    logging.basicConfig(level=logging.INFO)


def make_argparser():
    """Create a parser instance for this tool's options."""
    parser = argparse.ArgumentParser(description=__doc__.split('\n    Copyright ', 1)[0])

    parser.add_argument('-V', '--version', action='store_true', default=False,
                        help="show version number and exit")
    parser.add_argument('-q', '--quiet', action='store_true', default=False,
                        help="reduce logging output")
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help="increase logging output")

    args = parser.parse_args()

    if args.version:
        print(__version__)
        sys.exit(0)

    if args.verbose and args.quiet:
        parser.error("Cannot be both quiet and verbose!")
    elif args.quiet:
        logging.getLogger().setLevel(logging.WARNING)
    elif args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    return parser, args


def mainloop(parser, args):
    """Implementation of this command."""
    print(repr(args))
    for _ in range(30):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)


def run():
    """Execute main loop."""
    try:
        setup()
        try:
            parser, args = make_argparser()
            mainloop(parser, args)
        except KeyboardInterrupt as exc:
            sys.stderr.flush()
            sys.exit(2)
        except IOError as exc:
            if exc.errno == errno.EPIPE:  # downstream is done with our output
                sys.stderr.flush()
                sys.exit(0)
            else:
                raise
    finally:
        logging.shutdown()


if __name__ == '__main__':
    run()
