import math
from typing import Callable

import pyaudio

def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            print(args, kwargs)
            return dec(f, *args, **kwargs)

        return repl

    return layer

class Synthesizer:
    def __init__(self, channels=1, bitrate=44100, base_frequency=440):
        self.__bitrate = bitrate
        self.__channels = channels
        self.base_frequency = base_frequency

        self.__samples = []

        self.__pyaudio = pyaudio.PyAudio()

    def commit(self):
        self.__normalizeSamples()
        stream = self.__pyaudio.open(
                format=self.__pyaudio.get_format_from_width(1),
                channels=self.__channels,
                rate=self.__bitrate,
                output=True)

        stream.write(bytes(self.__samples))
        stream.stop_stream()
        stream.close()
        self.__samples = []

    def createSoundWithFunction(self, func: Callable, length: int or float) -> None:
        sample_amount = int(length * self.__bitrate)

        function = self.correct_frequency(func)
        print(function)

        for x in range(sample_amount):
            self.__samples.append(function(x))



    def __normalizeSamples(self):
        smallest = min(self.__samples)
        biggest = max(self.__samples)

        new = [(i - smallest) / (biggest - smallest) for i in self.__samples]

        self.__samples = [int(255 * x) for x in new]

    def __del__(self):
        print(f"Deleting {self}!")
        self.__pyaudio.terminate()
        del self



    def correct_frequency(self, func):
        amount_of_samples = self.__bitrate / self.base_frequency

        return lambda x: func(x / (amount_of_samples / (2 * math.pi)))


