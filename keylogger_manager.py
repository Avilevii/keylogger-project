# import json
#
# x={"name":"yosef","age":24,"city":"Jerusalem"}
# y=json.dumps(x)
# print(x)

#
# def check_positive(number):
#     if number<0:
#         raise ValueError("the number is negativ")
#     return number
# print(check_positive(5))

import time
import threading


class FileWriter:
    def write(self, data):
        with open('output.txt', 'a') as f:
            f.write(data + "\n")
        print(f"נכתב לקובץ: {data}")


class NetworkWriter:
    def write(self, data):
        print(f"שלח לרשת: {data}")


class InputCollector:
    def init(self, interval, file_writer, network_writer=None):
        self.buffer = []
        self.interval = interval
        self.file_writer = file_writer
        self.network_writer = network_writer
        self.lock = threading.Lock()
        self.stop_event = threading.Event()

    def collect_input(self):
        while not self.stop_event.is_set():
            user_input = input(f"הקלד משהו (בהפסקה של {self.interval} שניות): ")

            with self.lock:
                self.buffer.append(user_input)

            if len(self.buffer) > 0:
                self.process_buffer()

            time.sleep(self.interval)

    def process_buffer(self):
        with self.lock:
            data_to_write = ' '.join(self.buffer)
            self.file_writer.write(data_to_write)

            if self.network_writer:
                self.network_writer.write(data_to_write)

            self.buffer.clear()

    def stop(self): self.stop_event.set()

file_writer = FileWriter()
network_writer = NetworkWriter()

interval = 5
input_collector = InputCollector(interval, file_writer, network_writer)

input_thread = threading.Thread(target=input_collector.collect_input)
input_thread.start()

time.sleep(20)
input_collector.stop()
input_thread.join()













