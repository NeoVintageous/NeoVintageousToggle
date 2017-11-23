from sublime import load_settings
from sublime import save_settings
from sublime import status_message
import sublime_plugin


class ToggleNeovintageousCommand(sublime_plugin.ApplicationCommand):

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
