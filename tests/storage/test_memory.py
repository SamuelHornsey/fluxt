import pytest

from fluxt.storage import Memory


@pytest.fixture
def memory():
    return Memory()


def test_set_key(memory):
    memory.set_key('key', 1)

    assert memory.state['key'] == 1


def test_get_key(memory):
    memory.set_key('key', 1)

    val = memory.get_key('key')

    assert val == 1

    with pytest.raises(KeyError):
        memory.get_key('test')


def test_reset(memory):
    memory.set_key('key', 1)

    memory.reset()

    assert not memory.state
