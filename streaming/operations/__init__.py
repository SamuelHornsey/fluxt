from streaming.operations.filter import FilterFunction, \
    filter_function_generator
from streaming.operations.map import MapFunction, \
    map_function_generator
from streaming.operations.flat_map import FlatMapFunction, \
    flat_map_function_generator
from streaming.operations.reduce import ReducerFunction, \
    reducer_function_generator


def filter(*args, **kwargs):
    """ filter function decorator """
    def inner(func):
        return filter_function_generator(func)
    return inner


def flat_map(*args, **kwargs):
    """ flat map function decorator """
    def inner(func):
        return flat_map_function_generator(func)
    return inner


def map(*args, **kwargs):
    """ map function decorator """
    def inner(func):
        return map_function_generator(func)
    return inner


def reducer(*args, **kwargs):
    """ reducer function decorator """
    def inner(func):
        return reducer_function_generator(func)
    return inner
