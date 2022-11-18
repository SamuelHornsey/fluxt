from abc import ABC, abstractmethod


class Operation(ABC):
    """ base operation """

    def __init__(self, handler_func=None):
        """ base operation init """
        self.storage_backend = None
        self.handler_func = handler_func

    def __call__(self, event_collection):
        """_summary_

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

    def keyed_event(self, key, data):
        """ return a keyed event """
        return (key, data)
