import pytest

from fluxt.app.datastream import DataStream, DataStreamException
from fluxt.sources import CollectionSource
from fluxt.sinks import StdoutSink

import fluxt.operations as operations


class Map(operations.MapFunction):
    """ example map function """

    def map(self, event):
        return super().map(event)


class Filter(operations.FilterFunction):
    """ example filter function """

    def filter(self, event):
        return super().filter(event)


class FlatMap(operations.FlatMapFunction):
    """ example flat map function """

    def flat_map(self, event):
        return super().flat_map(event)


class Reduce(operations.ReducerFunction):
    """ example reducer function """

    def reduce(self, key, reduced, event):
        if not reduced:
            return event
        return event + reduced


class KeyBy(operations.KeyByFunction):
    """ example key by function """

    def key_by(self, event):
        return super().key_by(event)


def test_add_source():
    datastream = DataStream()
    datastream.add_source('source')
    assert datastream.source == 'source'


def test_add_sink():
    datastream = DataStream()
    datastream.add_sink('sink')
    assert datastream.sink == 'sink'


def test_source_from_collection():
    datastream = DataStream()
    datastream.source_from_collection([1, 2, 3])
    assert isinstance(datastream.source, CollectionSource)


def test_print():
    datastream = DataStream()
    datastream.print()
    assert isinstance(datastream.sink, StdoutSink)


def test_map():
    datastream = DataStream()
    datastream.map(Map())
    assert len(datastream.transformations) == 1

    with pytest.raises(TypeError) as e:
        datastream.map(Filter())

    assert "is not type MapFunction" in str(e)


def test_filter():
    datastream = DataStream()
    datastream.filter(Filter())
    assert len(datastream.transformations) == 1

    with pytest.raises(TypeError) as e:
        datastream.filter(Map())

    assert "is not type FilterFunction" in str(e)


def test_flat_map():
    datastream = DataStream()
    datastream.flat_map(FlatMap())
    assert len(datastream.transformations) == 1

    with pytest.raises(TypeError) as e:
        datastream.flat_map(Map())

    assert "is not type FlatMapFunction" in str(e)


def test_reduce():
    datastream = DataStream()
    datastream.reduce(Reduce())
    assert len(datastream.transformations) == 1

    with pytest.raises(TypeError) as e:
        datastream.reduce(FlatMap())

    assert "is not type ReducerFunction" in str(e)


def test_key_by():
    datastream = DataStream()
    datastream.key_by(KeyBy())
    assert len(datastream.transformations) == 1

    with pytest.raises(TypeError) as e:
        datastream.key_by(FlatMap())

    assert "is not type KeyByFunction" in str(e)


def test_pipeline():
    datastream = DataStream()
    datastream.pipeline(Map(), Filter(), Reduce())

    assert len(datastream.transformations) == 3

    with pytest.raises(TypeError) as e:
        datastream.pipeline(None, 'test')

    assert "is not type Operation" in str(e)


def test_execute_no_source():
    ds = DataStream()

    with pytest.raises(DataStreamException) as e:
        ds.execute()

    assert 'source not defined' in str(e)


def test_execute_no_sink():
    ds = DataStream()

    ds.source_from_collection([1, 2, 3])

    with pytest.raises(DataStreamException) as e:
        ds.execute()

    assert 'sink not defined' in str(e)


def test_execute(monkeypatch):
    agg = []

    def mock_pipe_capture(event_collection):
        for event in event_collection.events:
            agg.append(event)

    ds = DataStream()

    ds.source_from_collection([1, 2, 3])
    ds.print()

    monkeypatch.setattr(ds.sink, 'pipe', mock_pipe_capture)

    ds.filter(Filter()) \
        .map(Map())

    ds.execute()

    assert agg == [1, 2, 3]
