from abc import abstractmethod

from fluxt.operations.base import Operation


def filter_function_generator(func):
    class TempFilter(FilterFunction):
        def filter(self, event):
            return func(event)

    return TempFilter()


class FilterFunction(Operation):
    """ filter function class """

    def process_batch(self, events):
        """ passes a batch of events to filter

        Args:
            events (list): list of events

        Returns:
            batch (list): list of modified events
        """
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
