from abc import ABC, abstractmethod

class FilterFunction(ABC):
    """ filter function class """

    def __init__(self):
        """ init filter function """
        pass
    
    def __call__(self, event):
        """ call filter function """
        return self.filter(event)
    
    @property
    def type(self):
        """ return the operation type """
        return self.__class__.__base__.__name__

    @abstractmethod
    def filter(self, event):
        """ implements a filter function

        Args:
            event (object): event object

        Returns:
            boolean: bool if event should be returned
        """
        return True