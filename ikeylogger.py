from abc import ABC, abstractmethod

class IKeyLogger(ABC):
    @abstractmethod
    def start_logging(self):
        pass

    @abstractmethod
    def stop_logging(self):
        pass

    @abstractmethod
    def get_logged_keys(self):
        pass