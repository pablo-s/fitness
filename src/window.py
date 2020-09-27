# window.py
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

from gi.repository import GObject, Gtk, Handy

from .activity import Activity
from .history import History
from .record_activity_dialog import RecordActivityDialog


@Gtk.Template(resource_path='/com/github/pablo_s/fitness/window.ui')
class FitnessWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'FitnessWindow'

    _recordActivityButton = Gtk.Template.Child('record-activity')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._historyView = History()
        self.add(self._historyView)

        self._recordActivityButton.connect("clicked", self.record_activity)
        self.show_all()

    def record_activity(self, button):
        self._recordActivityDialog = RecordActivityDialog()
        self._recordActivityDialog.run()
        self._recordActivityDialog.destroy()

        activity = self._recordActivityDialog.recorded_activity()
        self._historyView.add_new_record(activity)
