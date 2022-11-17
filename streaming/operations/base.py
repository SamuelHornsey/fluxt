from abc import ABC


class Operation(ABC):
    """ base operation """

    def __init__(self):
        """ base operation init """
        self.storage_backend = None

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
