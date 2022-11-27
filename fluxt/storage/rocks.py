import rocksdb

from fluxt.storage.base import BaseStorage, SerializedPartition, \
    StorageException


class RocksDB(BaseStorage):
    """ rocksdb storage class """

    def __init__(self, datadir, **extra_options):
        """ init rocksdb storage """
        super().__init__()

        self.datadir = datadir

        if 'create_if_missing' in extra_options.keys() and \
                extra_options['create_if_missing'] is False:
            raise StorageException('rocksDB cannot be initialized with '
                                   'setting create_if_missing=False')

        self.extra_options = extra_options

    def path(self, partition):
        """ get the partition db path """
        return f'{self.datadir}/{partition}.db'

    def get_partition(self, partition):
        """ gets the partition db """
        try:
            return self.partitions[partition]
        except KeyError:
            self.partitions[partition] = RocksPartition(
                self.path(partition),
                self.extra_options)

            return self.partitions[partition]

    def _set(self, key, value, partition):
        """ sets a key """
        part = self.get_partition(partition)
        k, v = key.encode(), value.encode()
        part[k] = v

    def _get(self, key, partition):
        """ gets a key """
        part = self.get_partition(partition)
        k = key.encode()
        return part[k].decode()

    def _del(self, key, partition):
        """ delete a key """
        part = self.get_partition(partition)
        k = key.encode()
        del part[k]


class RocksPartition(SerializedPartition):
    """ rocksdb partition """

    def __init__(self, path, extra_options):
        """ init partition db """
        self.path = path
        self.db = rocksdb.DB(
            path,
            rocksdb.Options(
                create_if_missing=True,
                **extra_options))

    def __getitem__(self, key):
        value = self.db.get(key)
        if value:
            return value

        raise KeyError

    def __setitem__(self, key, value):
        self.db.put(key, value)

    def __delitem__(self, key):
        self.db.delete(key)
