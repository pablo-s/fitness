# activity.py
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

from gi.repository import GObject


class Activity(GObject.Object):
    def __init__(self, name, startTime, duration, **kwargs):
        super().__init__(**kwargs)
        self._name = name
        self._startTime = startTime
        self._duration = duration

    def name(self):
        return self._name

    def start_time(self):
        return self._startTime

    def duration(self):
        return self._duration
