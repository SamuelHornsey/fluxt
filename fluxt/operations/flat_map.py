from abc import ABC, abstractmethod

from fluxt.operations.base import Operation


def flat_map_function_generator(func):
    class TempFlatMap(FlatMapFunction):
        def flat_map(self, event):
            return func(event)

    return TempFlatMap()


class FlatMapFunction(Operation):
    """ flat map function class """

    def process_batch(self, events):
        """ passes a batch of events to flat map

        Args:
            events (list): list of events

        Returns:
            batch (list): list of modified events
        """
        batch = []
        for event in events:
            batch += self.flat_map(event)

        return batch

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
