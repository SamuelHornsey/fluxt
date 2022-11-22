import pytest

from fluxt.operations import KeyByFunction, key_by
from fluxt.app.events import EventCollection


class KeyBy(KeyByFunction):
    def key_by(self, event):
        return event[0], event[1]


class BadKeyBy(KeyByFunction):
    pass


def test_key_by_call():
    key_by_function = KeyBy()
    event_collection = EventCollection(None)
    event_collection.events = [('test', 1), ('test', 1), ('hello', 1)]
    event_collection = key_by_function(event_collection)

    assert len(event_collection.events) == 3


def test_key_by_type():
    key_by_function = KeyBy()
    assert key_by_function.type == 'KeyByFunction'


def test_decorated_key_by():
    @key_by()
    def my_key_by(event):
        return event, 1

    event_collection = EventCollection(None)
    event_collection.events = ['test', 'test', 'world']

    assert my_key_by(event_collection).events == [
        ('test', 1), ('test', 1), ('world', 1)]


def test_key_by_function():
    key_by_function = KeyBy()
    event_collection = key_by_function.key_by(('test', 1))

    # will return tuple so len == 2
    assert len(event_collection) == 2
    assert event_collection == ('test', 1)


def test_key_by_function_abstract():
    with pytest.raises(TypeError):
        BadKeyBy()
