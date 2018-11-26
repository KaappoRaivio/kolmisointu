import math

import note
from synthesizer import Synthesizer


def sound(*notes, tuning=440):
    print(notes)
    return lambda x: sum((math.sin(i.frequency(tuning) * x)) for i in notes)


synthesizer = Synthesizer(base_frequency=1, channels=1)

synthesizer.createSoundWithFunction(sound(note.Note("A4"), note.Note("C#5"), note.Note("E5")), 1)
synthesizer.commit()
