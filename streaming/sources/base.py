from abc import ABC, abstractmethod

class Source(ABC):
    @abstractmethod
    def generate(self):
        pass