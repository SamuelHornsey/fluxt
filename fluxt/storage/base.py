from abc import ABC, abstractmethod


class StorageException(Exception):
    pass


class BaseStorage:
    def __init__(self):
        self.partitions = {}

    @abstractmethod
    def _set(self, key, value, patition):
        pass

    @abstractmethod
    def _get(self, key, partition):
        pass

    @abstractmethod
    def _del(self, key):
        pass

    @abstractmethod
    def get_partition(self, partition):
        pass

    def get_key(self, key, partition):
        return self._get(key, partition)

    def set_key(self, key, value, partition):
        return self._set(key, value, partition)

    def del_key(self, key, partition):
        return self._del(key, partition)


class SerializedPartition:
    pass
