import pytest

from fluxt.operations import FilterFunction, filter
from fluxt.app.events import EventCollection


class GoodFilterFunction(FilterFunction):
    def filter(self, event):
        return True


class BadFilterFunction(FilterFunction):
    pass


def test_filter_call():
    filter_function = GoodFilterFunction()
    event_collection = EventCollection(None)
    event_collection.events = [1, 2, 3]
    event_collection = filter_function(event_collection)

    assert event_collection.events == [1, 2, 3]


def test_filter_type():
    filter_function = GoodFilterFunction()
    assert filter_function.type == 'FilterFunction'


def test_decorated_filter():
    @filter()
    def my_filter(event):
        return True

    event_collection = EventCollection(None)
    event_collection.events = [1, 2, 3]

    assert my_filter(event_collection)


def test_filter_function():
    filter_function = GoodFilterFunction()
    assert filter_function.filter({'event': 'test'})


def test_filter_function_abstract():
    with pytest.raises(TypeError):
        BadFilterFunction()
