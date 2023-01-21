import pytest

from fluxt.app.datastream import DataStream, DataStreamException
from fluxt.state import State
from fluxt.sources.base import Source
from fluxt.sinks.base import Sink


class TestSource(Source):
    def generate(self):
        return super().generate()


class TestSink(Sink):
    def pipe(self, event):
        return super().pipe(event)


class TestStore():
    def recover_state(self, partition_key):
        return {}


@pytest.fixture()
def ds():
    return DataStream('my_ds', TestStore())


def test_source_from_collection(ds):
    ds.source_from_collection([1, 2, 3])

    assert ds.source
    assert isinstance(ds.source, Source)
    assert ds.source.collection == [1, 2, 3]


def test_print(ds):
    ds.print()

    assert ds.sink
    assert isinstance(ds.sink, Sink)


def test_add_source(ds):
    ds.add_source(TestSource())
    assert isinstance(ds.source, TestSource)


def test_add_sink(ds):
    ds.add_sink(TestSink())
    assert isinstance(ds.sink, TestSink)


def test_pipeline(ds):
    def my_handler(event, output):
        pass

    ds.pipeline((my_handler, None))

    assert len(ds.operations) == 1

    with pytest.raises(TypeError):
        ds.pipeline((my_handler, 'not state'))

    state = State('name', default=10, value_type=None)

    ds.pipeline((my_handler, state))

    assert len(ds.operations) == 2


def test_execute(ds):
    with pytest.raises(DataStreamException):
        ds.execute()

    ds.source_from_collection([1, 2, 3])

    with pytest.raises(DataStreamException):
        ds.execute()
