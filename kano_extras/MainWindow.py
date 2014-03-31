# kano-extras
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# The MainWindow class

import os
from gi.repository import Gtk, Gdk

from kano_extras import Media
from kano_extras.UIElements import TopBar, AppGrid, AppGridEntry
from kano_extras.AppData import get_applications

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Kano Extras')

        screen = Gdk.Screen.get_default()
        self._win_width = 800
        self._win_height = int(screen.get_height() * 0.5)

        self.set_decorated(False)
        self.set_resizable(False)
        self.set_size_request(self._win_width, self._win_height)

        self.set_position(Gtk.WindowPosition.CENTER)

        self.connect('delete-event', Gtk.main_quit)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(Media.media_dir() + 'css/style.css')
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, css_provider,
                                              Gtk.STYLE_PROVIDER_PRIORITY_USER)

        self._grid = Gtk.Grid()

        self._top_bar = TopBar()
        self._grid.attach(self._top_bar, 0, 0, 1, 1)

        self._apps = AppGrid()

        apps = get_applications()
        for app in apps:
            self._apps.add_entry(app['Name'], app['Comment[en_GB]'],
                                 app['Icon'], app['Exec'])
        self._grid.attach(self._apps, 0, 1, 1, 1)

        self._grid.set_row_spacing(0)

        self.add(self._grid)