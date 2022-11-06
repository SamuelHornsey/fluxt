from abc import ABC, abstractmethod

class Sink(object):
    @abstractmethod
    def pipe(self, event):
        pass