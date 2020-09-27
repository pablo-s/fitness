# record_activity_dialog.py
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


@Gtk.Template(resource_path='/com/github/pablo_s/fitness/record_activity_dialog.ui')
class RecordActivityDialog(Gtk.Dialog):
    __gtype_name__ = 'RecordActivityDialog'

    _startStopRecordingButton = Gtk.Template.Child('start-stop-recording')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._recordingStarted = False
        self._recordingStartTime = None
        self._recordedActivity = None
        self._startStopRecordingButton.connect("clicked", self.startStopRecording)

    def recorded_activity(self):
        return self._recordedActivity

    def startStopRecording(self, button):
        if not self._recordingStarted:
            self._recordingStarted = True
            self._recordingStartTime = datetime.now()
            self._startStopRecordingButton.set_label('Stop')
        else:
            recordingStopTime = datetime.now()
            activityDuration = recordingStopTime - self._recordingStartTime
            self._recordedActivity = Activity('Running',
                                              self._recordingStartTime,
                                              activityDuration)
            self.close()
