from pynput import keyboard

KEYS_INTERESTED = "wasdqe"

class KeyboardListener:
    def __init__(self, keys_interested=None):
        self.listener = keyboard.Listener(on_press=self._onPress, on_release=self._onRelease)
        self.listener.start()
        self.listener.wait()

        self.keys_down = set({})

        if keys_interested is not None:
            self.keys_interested = keys_interested
        else:
            self.keys_interested = None

    def _onPress(self, key):
        try:
            k = key.char
        except AttributeError:
            k = key.name

        if self.keys_interested is None:
            self.keys_down.add(k)

        elif k is not None and k in KEYS_INTERESTED :
            self.keys_down.add(k)

        print(self.keys_down)
        return True


    def _onRelease(self, key):
        try:
            k = key.char  # single-char keys
        except AttributeError:
            k = key.name  # other keys

        if self.keys_interested is None:
            self.keys_down.remove(k)

        elif k is not None and k in KEYS_INTERESTED:
            self.keys_down.remove(k)

        print(self.keys_down)
        return True

a = KeyboardListener()
a.listener.join()