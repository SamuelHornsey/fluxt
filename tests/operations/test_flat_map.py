import pytest

from streaming.operations import FlatMapFunction


class FlatMap(FlatMapFunction):
    def flat_map(self, event):
        return event.split(' ')


class BadFlatMap(FlatMapFunction):
    pass


def test_flat_map_call():
    flat_map_function = FlatMap()
    event_collection = flat_map_function(['text', 'text', 'some text'])

    assert len(event_collection) == 4
    assert event_collection == ['text', 'text', 'some', 'text']


def test_flat_map_type():
    flat_map_function = FlatMap()
    assert flat_map_function.type == 'FlatMapFunction'


def test_flat_map_function():
    flat_map_function = FlatMap()
    event_collection = flat_map_function.flat_map('test text')

    assert len(event_collection) == 2
    assert event_collection == ['test', 'text']


def test_flat_map_function_abstract():
    with pytest.raises(TypeError):
        BadFlatMap()
