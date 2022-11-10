from abc import ABC, abstractmethod

class MapFunction(ABC):
    """ map function class """

    def __init__(self):
        pass
    
    def __call__(self, event):
        return self.map(event)

    @abstractmethod
    def map(self, event):
        """ implements a map function

        Args:
            event (object): event object

        Returns:
            object: event object
        """
        return event