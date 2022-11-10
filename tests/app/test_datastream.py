import pytest

from streaming.app.datastream import DataStream
from streaming.sources import CollectionSource
from streaming.sinks import StdoutSink

import streaming.operations as operations

class Map(operations.MapFunction):
    """ example map function """
    def map(self, event):
        return super().map(event)

class Filter(operations.FilterFunction):
    """ example filter function """
    def filter(self, event):
        return super().filter(event)

@pytest.fixture(scope='function')
def datastream():
    return DataStream()

def test_add_source(datastream):
    datastream.add_source('source')
    assert datastream.source == 'source'

def test_add_sink(datastream):
    datastream.add_sink('sink')
    assert datastream.sink == 'sink'

def test_source_from_collection(datastream):
    datastream.source_from_collection([1, 2, 3])
    assert isinstance(datastream.source, CollectionSource)

def test_print(datastream):
    datastream.print()
    assert isinstance(datastream.sink, StdoutSink)

def test_map(datastream):
    datastream.map(Map())
    assert len(datastream.transformations) == 1

    with pytest.raises(TypeError):
        datastream.map(Filter())

def test_filter(datastream):
    datastream.filter(Filter())
    assert len(datastream.transformations) == 2

    with pytest.raises(TypeError):
        datastream.filter(Map())

