import math
import pyaudio
import subprocess

from synthesizer import Synthesizer


def f(x):
    return math.sin(x) + math.sin(x * (2 ** (4/12))) + math.sin(x * (2 ** (7/12))) + math.sin(x * (2 ** (12 /12))) * 0.8

def g(x):
    return math.sin(x * (2 ** (-3/12))) + math.sin(x) + math.sin(x * (2 ** (4/12))) + math.sin(x * (2 ** (9 /12)))

def h(x):
    return math.sin(x * (2 ** (-7/12))) + math.sin(x) + math.sin(x * (2 ** (5/12))) + math.sin(x * (2 ** (9 / 12)))

def i(x):
    return math.sin(x * (2 ** (7/12))) + math.sin(x * (2 ** (-1 / 12))) + math.sin(x * (2 ** (2 / 12))) + math.sin(x * (2 ** (7 / 12)))

synthesizer = Synthesizer(base_frequency=440)
synthesizer.createSoundWithFunction(f, 0.5)
synthesizer.createSoundWithFunction(g, 1)
synthesizer.createSoundWithFunction(h, 0.5)
synthesizer.createSoundWithFunction(i, 0.5)
synthesizer.createSoundWithFunction(f, 0.5)
synthesizer.createSoundWithFunction(g, 0.5)
synthesizer.createSoundWithFunction(h, 0.5)
synthesizer.createSoundWithFunction(i, 0.5)


synthesizer.commit()