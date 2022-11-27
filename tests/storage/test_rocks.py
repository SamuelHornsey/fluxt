import pytest
import rocksdb

from fluxt.storage import RocksDB
from fluxt.storage.base import StorageException

DATADIR = '/tmp/data'


def test_start_rocks_storage():
    store = RocksDB(DATADIR)

    assert store.datadir == DATADIR

    with pytest.raises(StorageException):
        store = RocksDB(DATADIR, create_if_missing=False)


def test_get_partition():
    store = RocksDB(DATADIR)

    partition = store.get_partition('my-partition')

    assert partition.path == f'{DATADIR}/my-partition.db'


def test_set_key():
    store = RocksDB(DATADIR)

    store.set_key('mykey', 'value', 'my-partition')
    key = store.get_key('mykey', 'my-partition')

    assert key == 'value'


def test_get_key():
    store = RocksDB(DATADIR)
    value = store.get_key('mykey', 'my-partition')
    assert value == 'value'


def test_delete_key():
    store = RocksDB(DATADIR)

    store.set_key('mykey', 'value', 'my-partition')
    store.del_key('mykey', 'my-partition')

    with pytest.raises(KeyError):
        store.get_key('mykey', 'my-partition')
