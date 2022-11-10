from abc import ABC, abstractmethod

class FilterFunction(ABC):
    """ filter function class """

    def __init__(self):
        pass
    
    def __call__(self, event):
        return self.filter(event)

    @abstractmethod
    def filter(self, event):
        """ implements a filter function

        Args:
            event (object): event object

        Returns:
            object: event object
        """
        return event