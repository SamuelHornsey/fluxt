from fluxt.storage.base import BaseStorage, SerializedPartition


class Memory(BaseStorage):
    def _set(self, key, value, partition):
        part = self.get_partition(partition)
        part[key] = value

    def _get(self, key, partition):
        part = self.get_partition(partition)
        return part[key]

    def _del(self, key, partition):
        part = self.get_partition(partition)
        del part[key]

    def get_partition(self, partition):
        try:
            return self.partitions[partition]
        except KeyError:
            self.partitions[partition] = MemoryPartition()
            return self.partitions[partition]


class MemoryPartition(SerializedPartition):
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __delitem__(self, key):
        del self.data[key]
