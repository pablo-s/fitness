# main.py
#
# Copyright 2020 Pablo Sánchez Rodríguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '1')

from gi.repository import GObject, Gtk, Gio, Handy

from .window import FitnessWindow


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='com.github.pablo_s.fitness',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        Handy.init()
        win = self.props.active_window
        if not win:
            win = FitnessWindow(application=self)
        win.present()

def main(version):
    app = Application()
    return app.run(sys.argv)