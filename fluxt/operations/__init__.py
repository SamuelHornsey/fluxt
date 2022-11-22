from fluxt.operations.filter import FilterFunction, \
    filter_function_generator
from fluxt.operations.map import MapFunction, \
    map_function_generator
from fluxt.operations.flat_map import FlatMapFunction, \
    flat_map_function_generator
from fluxt.operations.reduce import ReducerFunction, \
    reducer_function_generator
from fluxt.operations.key import KeyByFunction, \
    key_by_function_generator


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


def key_by(*args, **kwargs):
    """ key by function decorator """
    def inner(func):
        return key_by_function_generator(func)
    return inner
