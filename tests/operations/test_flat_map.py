import pytest

from fluxt.operations import FlatMapFunction, flat_map
from fluxt.app.events import EventCollection


class FlatMap(FlatMapFunction):
    def flat_map(self, event):
        return event.split(' ')


class BadFlatMap(FlatMapFunction):
    pass


def test_flat_map_call():
    flat_map_function = FlatMap()
    event_collection = EventCollection(None)
    event_collection.events = ['text', 'text', 'some text']
    event_collection = flat_map_function(event_collection)

    assert len(event_collection.events) == 4
    assert event_collection.events == ['text', 'text', 'some', 'text']


def test_flat_map_type():
    flat_map_function = FlatMap()
    assert flat_map_function.type == 'FlatMapFunction'


def test_decorated_flat_map():
    @flat_map()
    def my_flat_map(event):
        return []

    event_collection = EventCollection(None)
    event_collection.events = [1, 2, 3]

    assert my_flat_map(event_collection).events == []


def test_flat_map_function():
    flat_map_function = FlatMap()
    event_collection = flat_map_function.flat_map('test text')

    assert len(event_collection) == 2
    assert event_collection == ['test', 'text']


def test_flat_map_function_abstract():
    with pytest.raises(TypeError):
        BadFlatMap()
