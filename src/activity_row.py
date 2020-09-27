# activity_row.py
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

from datetime import datetime
from gi.repository import GObject, Gtk, Handy

from .activity import Activity


@Gtk.Template(resource_path='/com/github/pablo_s/fitness/activity_row.ui')
class ActivityRow(Gtk.ListBoxRow):
    __gtype_name__ = 'ActivityRow'

    _icon = Gtk.Template.Child('icon')
    _name = Gtk.Template.Child('activity-name')
    _startTime = Gtk.Template.Child('activity-start-time')
    _duration = Gtk.Template.Child('activity-duration')

    def __init__(self, activity, **kwargs):
        super().__init__(**kwargs)

        self._icon.set_from_icon_name('location-services-active-symbolic', Gtk.IconSize.DIALOG)
        self._name.set_label(activity.name())

        self._startTime.set_label(activity.start_time().strftime('%H:%M:%S'))
        self._date = activity.start_time().strftime('%d/%m/%Y')
        self._duration.set_label(str(activity.duration()).split('.')[0])

    def show_header(self):
        self.set_header(Gtk.Label(self._date))
