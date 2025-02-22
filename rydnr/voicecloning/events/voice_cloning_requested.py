# vim: set fileencoding=utf-8
"""
rydnr/voicecloning/events/voice_cloning_requested.py

This file defines VoiceCloningRequested class.

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
from pythoneda.shared import Event


class VoiceCloningRequested(Event):
    """
    A recording of a cloned voice reading a text is requested.

    Class name: VoiceCloningRequested

    Responsibilities:
        - Represent the moment in which the recording has been requested.

    Collaborators:
        - None
    """

    def __init__(self, audioFile: str, textFile: str, outputFile: str):
        """
        Creates a new VoiceCloningRequested instance.
        :param audioFile: The audio file.
        :type audioFile: str
        :param textFile: The text file.
        :type textFile: str
        :param outputFile: The output file.
        :type outputFile: str
        """
        super().__init__()
        self._audio_file = audioFile
        self._text_file = textFile
        self._output_file = outputFile

    @property
    def audio_file(self) -> str:
        """
        Retrieves the audio file.
        :return: The audio file.
        :rtype: str
        """
        return self._audio_file

    @property
    def text_file(self) -> str:
        """
        Retrieves the text file.
        :return: The text file.
        :rtype: str
        """
        return self._text_file

    @property
    def output_file(self) -> str:
        """
        Retrieves the output file.
        :return: Such file.
        :rtype: str
        """
        return self._output_file
