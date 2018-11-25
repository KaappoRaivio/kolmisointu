import math
import pyaudio
import subprocess

from synthesizer import Synthesizer


def f(x):
    return math.sin(x) + math.sin(x * (2 ** (3/12))) + math.sin(x * (2 ** (7/12))) + math.sin(x * (2 ** (10 /12))) * 0.8

def g(x):
    return math.sin(x) + math.sin(x * (2 ** (4/12))) + math.sin(x * (2 ** (7/12))) + math.sin(x * (2 ** (11 /12)))

synthesizer = Synthesizer(base_frequency=440)
synthesizer.createSoundWithFunction(f, 0.5)
synthesizer.createSoundWithFunction(g, 0.5)
synthesizer.commit()