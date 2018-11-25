import math
import pyaudio
import subprocess

from synthesizer import Synthesizer


def a(x):
    return math.sin(x) + math.sin(x * (2 ** (7/12))) * 1.5 + math.sin(x * (2 ** (12/12))) + math.sin(x * (2 ** (16/12))) * 0.8

def gsharp(x):
    return math.sin(x * (2 ** (-1/12))) * 1.5 + math.sin(x * (2 ** (6/12))) + math.sin(x * (2 ** (11/12))) + math.sin(x * (2 ** (14 /12)))

def csharp(x):
    return math.sin(x * (2 ** (4/12))) * 1.5 + math.sin(x * (2 ** (11/12))) + math.sin(x * (2 ** (14/12))) + math.sin(x * (2 ** (19 / 12)))

def i(x):
    return math.sin(x * (2 ** (-5/12)))  + math.sin(x * (2 ** (-1 / 12))) + math.sin(x * (2 ** (2 / 12))) + math.sin(x * (2 ** (7 / 12)))

synthesizer = Synthesizer(base_frequency=440)

funcs = [a, gsharp, csharp, i]

i = 0

synthesizer.createSoundWithFunction(a, 1)
synthesizer.createSoundWithFunction(a, 1.5)
synthesizer.createSoundWithFunction(gsharp, 0.5)
synthesizer.createSoundWithFunction(csharp, 2)
synthesizer.commit()
# while True:
#     func = funcs[i % len(funcs)]
#
#     synthesizer.createSoundWithFunction(func, 1)
#     synthesizer.commit()
#     i += 1


