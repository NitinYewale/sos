# Copyright (C) 2019 Red Hat, Inc., Jake Hunsaker <jhunsake@redhat.com>

# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.report.plugins import Plugin, RedHatPlugin


class Rasdaemon(Plugin, RedHatPlugin):

    short_desc = 'rasdaemon kernel trace event monitor'

    plugin_name = 'rasdaemon'
    packages = ('rasdaemon', )
    services = ('rasdaemon', )

    def setup(self):
        subcmds = [
            '--errors',
            '--guess-labels',
            '--layout',
            '--mainboard',
            '--print-labels',
            '--status',
            '--summary'
        ]
        self.add_cmd_output([f"ras-mc-ctl {sub}" for sub in subcmds])

# vim: set et ts=4 sw=4 :
