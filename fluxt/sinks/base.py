from abc import ABC, abstractmethod


class Sink(ABC):
    @abstractmethod
    def pipe(self, event):
        """ pipe data abstract """
        pass
