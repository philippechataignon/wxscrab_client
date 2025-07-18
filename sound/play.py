#!/usr/bin/env python3

from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("fin_tour.wav")
play(song)
