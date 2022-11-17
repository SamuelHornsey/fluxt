import pytest

from streaming.operations import ReducerFunction
from streaming.storage import Memory


class GoodReduceFunction(ReducerFunction):
    def reduce(self, key, reduced, event):
        if reduced == None:
            return 1

        return reduced + event


class BadReduceFunction(ReducerFunction):
    pass


@pytest.fixture
def memory():
    return Memory()


def test_reduce_call(memory):
    test_reduce = GoodReduceFunction()
    test_reduce.storage = memory

    event_collection = test_reduce([('key', 1), ('key', 2), ('other', 1)])

    assert event_collection == [('key', 1), ('key', 3), ('other', 1)]


def test_reduce_type():
    test_reduce = GoodReduceFunction()
    assert test_reduce.type == 'ReducerFunction'


def test_reduce_function():
    test_reduce = GoodReduceFunction()
    event = test_reduce.reduce('key', 1, 2)

    assert event == 3


def test_reduce_function_abstract():
    with pytest.raises(TypeError):
        BadReduceFunction()
