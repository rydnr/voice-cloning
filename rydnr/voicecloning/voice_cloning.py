# vim: set fileencoding=utf-8
"""
rydnr/voicecloning/voice_cloning.py

This file defines VoiceCloning class.

Copyright (C) 2025-today rydnr's voice-cloning

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared import EventListener, listen
from rydnr.voicecloning.events import VoiceCloningRequested


class VoiceCloning(EventListener):
    """
    Manages the voice cloning process.

    Class name: VoiceCloning

    Responsibilities:
        - Perform voice cloning.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new VoiceCloning instance.
        """
        super().__init__()

    @classmethod
    @listen(VoiceCloningRequested)
    async def listen_VoiceCloningRequested(cls, event: VoiceCloningRequested):
        """
        Clones the voice.
        :param event: The event.
        :type event: rydnr.voicecloning.events.VoiceCloningRequested
        """
        print(
            f"Cloning voice from {event.audio_file} reading {event.text_file} to {event.output_file}"
        )
