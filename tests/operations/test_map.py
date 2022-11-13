import pytest

from streaming.operations import MapFunction


class GoodMapFunction(MapFunction):
    def map(self, event):
        return event


class BadMapFunction(MapFunction):
    pass


def test_map_type():
    test_map = GoodMapFunction()
    assert test_map.type == 'MapFunction'


def test_map_function():
    test_map = GoodMapFunction()
    event = test_map.map({'event': 'data'})

    assert event == {'event': 'data'}


def test_map_function_abstract():
    with pytest.raises(TypeError):
        BadMapFunction()
