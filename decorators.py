import math


def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer

@parametrized
def correct_frequency(func, bitrate, base_frequency):
    amount_of_samples = bitrate / base_frequency

    return lambda x: func(x /  (amount_of_samples / (2*math.pi)))