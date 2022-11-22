from abc import abstractmethod

from fluxt.operations.base import Operation


def key_by_function_generator(func):
    class TempKeyBy(KeyByFunction):
        def key_by(self, event):
            return func(event)

    return TempKeyBy()


class KeyByFunction(Operation):
    """ key the event stream """

    def process_batch(self, events):
        """ passes a batch of events to key

        Args:
            events (list): list of events

        Returns:
            batch (list): list of modified events
        """

        batch = []

        for event in events:
            key, value = self.key_by(event)
            batch.append((key, value))

        return batch

    @property
    def type(self):
        """ return the operation type """
        return self.__class__.__base__.__name__

    @abstractmethod
    def key_by(self, event):
        return True
