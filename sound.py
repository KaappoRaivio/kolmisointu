import math
import pyaudio
import subprocess

from decorators import correct_frequency



@correct_frequency(16000, 440)
def f(x):
    return math.sin(x) + math.sin(x * (2 ** (3/12))) + math.sin(x * (2 ** (7/12))) + math.sin(x * (2 ** (10 /12)))
    # return math.sin(x) + math.sin(1.2*x) + math.sin(1.5*x)


def normalize(array, _min=0, _max=1):

    smallest = min(array)
    biggest = max(array)

    new = [(i - smallest) / (biggest - smallest) for i in array]

    return [int(_min + (_max - _min) * x) for x in new]



bitrate = 16000
frequency = 550
length = 2

amount_of_frames = int(bitrate * length)
rest_of_frames = amount_of_frames % bitrate
amount_of_samples_per_oscillation = bitrate / frequency

wavedata = []

for x in range(amount_of_frames):
  data = f(x)
  wavedata.append(data)


for x in range(rest_of_frames):
 wavedata.append(0)

wavedata = normalize(wavedata, 0, 255)

p = pyaudio.PyAudio()
stream = p.open(format = p.get_format_from_width(1),
                channels = 1,
                rate = bitrate,
                output = True)

stream.write(bytes(bytearray(wavedata)))
stream.stop_stream()
stream.close()
p.terminate()