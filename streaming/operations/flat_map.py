from abc import ABC, abstractmethod

from streaming.operations.base import Operation


class FlatMapFunction(Operation):
    """ flat map function class """

    def __call__(self, event_collection):
        """ call flat map function """
        results = []
        for event in event_collection:
            results += self.flat_map(event)

        return results

    @property
    def type(self):
        """ return the operation type """
        return self.__class__.__base__.__name__

    @abstractmethod
    def flat_map(self, event):
        """ implements a flat map function

        Args:
            event (object): event object

        Returns:
            collection (list): list of events
        """
        return []
