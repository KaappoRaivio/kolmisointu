from math import log2


class Note:
    dictionary = {
        "Cb": 2 ** (-10 / 12),
        "C": 2 ** (-9/12),
        "C#": 2 ** (-8/12),
        "Db": 2 ** (-8/12),
        "D": 2 ** (-7/12),
        "D#": 2 ** (-6/12),
        "Eb": 2 ** (-6/12),
        "E": 2 ** (-5/12),
        "E#": 2 ** (-4/12),
        "Fb": 2 ** (-5/12),
        "F": 2 ** (-4/12),
        "F#": 2 ** (-3/12),
        "Gb": 2 ** (-3/12),
        "G": 2 ** (-2/12),
        "G#": 2 ** (-1/12),
        "Ab": 2 ** (-1/12),
        "A": 2 ** (0/12),
        "A#": 2 ** (1/12),
        "Bb": 2 ** (1/12),
        "B": 2 ** (2/12),
        "B#": 2 ** (3/12),

    }

    def __init__(self, string_repr):
        self.note, self.octave, = self.__parse_string(string_repr)[0], int(self.__parse_string(string_repr)[1])

    @staticmethod
    def __parse_string(string_repr):
        temp = list(string_repr)


        *note, octave = temp
        return ''.join(note), octave


    def frequency(self, tuning=440):
        A4 = tuning
        octave_frequency = A4 * 2 ** (self.octave - 4)
        return octave_frequency * self.dictionary[self.note]

a = Note("B#9")

print(a.frequency())