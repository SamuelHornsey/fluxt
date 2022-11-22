from abc import ABC, abstractmethod


class Operation(ABC):
    """ base operation """

    def __init__(self):
        """ base operation init """
        self.storage_backend = None

    def __call__(self, event_collection):
        """ run process batch execution

        Args:
            event_collection (list): list of events

        Returns:
            event_collection: list of events
        """
        results = self.process_batch(event_collection.events)

        event_collection.events = results

        return event_collection

    @abstractmethod
    def process_batch(self, events):
        """ process the incoming event batch """
        pass

    @property
    def storage(self):
        """ operation storage class """
        return self.storage_backend

    @storage.setter
    def storage(self, storage):
        """ set operation storage class """
        self.storage_backend = storage
