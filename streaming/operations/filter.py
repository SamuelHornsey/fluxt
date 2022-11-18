from abc import abstractmethod

from streaming.operations.base import Operation


class FilterFunction(Operation):
    """ filter function class """

    def process_batch(self, events):
        batch = []
        for event in events:
            if self.filter(event):
                batch.append(event)

        return batch

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
