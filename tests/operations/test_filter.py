import pytest

from streaming.operations import FilterFunction


class GoodFilterFunction(FilterFunction):
    def filter(self, event):
        return True


class BadFilterFunction(FilterFunction):
    pass


def test_filter_call():
    filter_function = GoodFilterFunction()
    event_collection = filter_function([1, 2, 3])

    assert event_collection == [1, 2, 3]


def test_filter_type():
    filter_function = GoodFilterFunction()
    assert filter_function.type == 'FilterFunction'


def test_filter_function():
    filter_function = GoodFilterFunction()
    assert filter_function.filter({'event': 'test'})


def test_filter_function_abstract():
    with pytest.raises(TypeError):
        BadFilterFunction()
