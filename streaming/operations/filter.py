from abc import abstractmethod

from streaming.operations.base import Operation


class FilterFunction(Operation):
    """ filter function class """

    def __call__(self, event_collection):
        """_summary_

        Args:
            event_collection (list): list of events

        Returns:
            event_collection: list of events
        """
        results = []
        for event in event_collection:
            if self.filter(event):
                results.append(event)

        return results

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
