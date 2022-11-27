from abc import ABC, abstractmethod


class Operation(ABC):
    """ base operation """

    def __init__(self):
        """ base operation init """
        self.storage_backend = None
        self.storage_partition_key = None

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

    @property
    def partition_key(self):
        return self.storage_partition_key

    @partition_key.setter
    def partition_key(self, partition):
        self.storage_partition_key = partition

    def storage_set(self, key, value):
        pass

    def storage_get(self, key):
        pass
