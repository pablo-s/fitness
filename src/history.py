# history.py
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

from gi.repository import GObject, Gio, Gtk, Handy

from .activity import Activity
from .activity_row import ActivityRow


@Gtk.Template(resource_path='/com/github/pablo_s/fitness/history.ui')
class History(Gtk.ScrolledWindow):
    __gtype_name__ = 'EventHistory'

    mylist = Gtk.Template.Child('box')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.listbox = Gtk.ListBox()
        Gtk.StyleContext.add_class(self.listbox.get_style_context(), 'content')
        self.mylist.pack_start(self.listbox, True, False, 0)

        self.model = Gio.ListStore.new(Activity)
        self.listbox.bind_model(self.model, self.create_activity_row)
        self.listbox.set_header_func(self.update_header)

    def add_new_record(self, activity):
        self.model.insert_sorted(activity,
                                 lambda a1, a2: a1 < a2)

    def create_activity_row(self, activity):
        return ActivityRow(activity)

    def update_header(self, activityRow, activityRowAbove):
        if activityRowAbove is None:
            activityRow.show_header()
        else:
            activityRow.hide_header()
