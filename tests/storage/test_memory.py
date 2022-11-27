import pytest

from fluxt.storage.memory import Memory, MemoryPartition


def test_start_memory_storage():
    memory = Memory()
    assert memory.partitions == {}


def test_get_partition():
    memory = Memory()
    partition = memory.get_partition('my-partition')

    assert 'my-partition' in memory.partitions.keys()
    assert isinstance(partition, MemoryPartition)


def test_set_key():
    memory = Memory()
    memory.set_key('key', 1, 'my-partition')
    assert memory.partitions['my-partition'].data
    assert memory.partitions['my-partition'].data['key'] == 1


def test_get_key():
    memory = Memory()
    memory.set_key('key', 1, 'my-partition')

    value = memory.get_key('key', 'my-partition')
    assert value == 1

    with pytest.raises(KeyError):
        memory.get_key('test', 'my-partition')


def test_delete_key():
    memory = Memory()
    memory.set_key('key', 1, 'my-partition')

    memory.del_key('key', 'my-partition')

    with pytest.raises(KeyError):
        memory.get_key('key', 'my-partition')
