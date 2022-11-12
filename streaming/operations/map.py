from abc import ABC, abstractmethod

class MapFunction(ABC):
    """ map function class """

    def __init__(self):
        """ init map function """
        pass
    
    def __call__(self, event):
        """ call map function """
        return self.map(event)

    @property
    def type(self):
        """ return the operation type """
        return self.__class__.__base__.__name__
    
    @abstractmethod
    def map(self, event):
        """ implements a map function

        Args:
            event (object): event object

        Returns:
            object: event object
        """
        return event