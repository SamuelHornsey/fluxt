from abc import abstractmethod

from fluxt.operations.base import Operation


def reducer_function_generator(func):
    class TempReducer(ReducerFunction):
        def reduce(self, event, state):
            return func(event, state)

    return TempReducer()


class ReducerFunction(Operation):
    """ reducer function class """

    def process_batch(self, events):
        """ passes a batch of events to reduce

        Args:
            events (list): list of events

        Returns:
            batch (list): list of modified events
        """
        batch = []
        print(self.table, self.table.state, self.table.change_log)
        for event in events:
            batch.append(self.reduce(event, self.table))
        return batch

    @property
    def type(self):
        """ return the operation type """
        return self.__class__.__base__.__name__

    @abstractmethod
    def reduce(self, event, state):
        """ abstract reducer """
        return event
