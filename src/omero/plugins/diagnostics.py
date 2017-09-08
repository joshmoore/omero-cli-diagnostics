#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2017 University of Dundee & Open Microscopy Environment.
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
   Plugin for printing all diagnostic messages
"""

import sys

from omero.cli import CLI
from omero.cli import BaseControl
from omero.cli import DiagnosticsControl

HELP = """Call diagnostics on all subplugins"""


class CollectingDiagnosticsControl(BaseControl):
    """
    """

    def _configure(self, parser):
        self.__parser__ = parser  # For formatting later
        parser.set_defaults(func=self.__call__)
        parser.add_argument(
            "--no-logs", action="store_true",
            help="Skip log parsing")
        # Argument list must match that of the
        # DiagnosticsControl._add_diagnostics method

    def __call__(self, args):
        for name, control in sorted(self.ctx.controls.items()):
            if isinstance(control, DiagnosticsControl):
                control.diagnostics(args)


try:
    register("diagnostics", CollectingDiagnosticsControl, HELP)
except NameError:
    if __name__ == "__main__":
        cli = CLI()
        cli.register("diagnostics", CollectingDiagnosticsControl, HELP)
        cli.invoke(sys.argv[1:])
