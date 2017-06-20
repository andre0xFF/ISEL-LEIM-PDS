#!/usr/bin/env python3
import sys
sys.path.append('../../PySynth')
import pysynth_s as pysynth

test = (('c', 4), ('e', 4), ('g', 4), ('c5', 1))
pysynth.make_wav(test)
