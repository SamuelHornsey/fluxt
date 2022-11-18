from streaming.operations.filter import FilterFunction
from streaming.operations.map import MapFunction
from streaming.operations.flat_map import FlatMapFunction
from streaming.operations.reduce import ReducerFunction


def map(*args, **kwargs):
    def inner(func):
        map_function = MapFunction(handler_func=func)
        return func
