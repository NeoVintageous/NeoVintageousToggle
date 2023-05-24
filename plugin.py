# Copyright (C) 2023 Gerard Roche
#
# This file is part of NeoVintageous.
#
# NeoVintageous is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NeoVintageous is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NeoVintageous.  If not, see <https://www.gnu.org/licenses/>.

from sublime import load_settings
from sublime import save_settings
from sublime import status_message
import sublime_plugin


class NeovintageousToggle(sublime_plugin.ApplicationCommand):

    def run(self):
        settings = load_settings('Preferences.sublime-settings')
        ignored_packages = settings.get('ignored_packages', [])

        if 'NeoVintageous' in ignored_packages:
            ignored_packages.remove('NeoVintageous')
            status = 'enabled'
        else:
            ignored_packages.append('NeoVintageous')
            status = 'disabled'

        ignored_packages.sort()
        settings.set('ignored_packages', ignored_packages)
        save_settings('Preferences.sublime-settings')

        status_message('NeoVintageous {}'.format(status))
