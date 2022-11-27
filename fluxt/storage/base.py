from abc import ABC, abstractmethod


class StorageException(Exception):
    pass


class BaseStorage(ABC):
    def __init__(self):
        """ base init storage """
        self.partitions = {}

    @abstractmethod
    def _set(self, key, value, patition):
        """ abstract set a key """
        pass

    @abstractmethod
    def _get(self, key, partition):
        """ abstract get a key """
        pass

    @abstractmethod
    def _del(self, key):
        """ abstract delete a key """
        pass

    @abstractmethod
    def get_partition(self, partition):
        """ returns the partition """
        pass

    def get_key(self, key, partition):
        """ get key """
        return self._get(key, partition)

    def set_key(self, key, value, partition):
        """ set key """
        return self._set(key, value, partition)

    def del_key(self, key, partition):
        """ delete key """
        return self._del(key, partition)


# TODO: complete
class SerializedPartition:
    pass
