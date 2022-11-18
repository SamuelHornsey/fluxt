import pytest

from streaming.app.graph import OperationNode, StreamGraph, graph_generator
from streaming.operations import FilterFunction, MapFunction, ReducerFunction
from streaming.app.events import EventCollection
from streaming.storage import Memory


class Map(MapFunction):
    def map(self, event):
        return super().map(event)


class Filter(FilterFunction):
    def filter(self, event):
        return super().filter(event)


class Reducer(ReducerFunction):
    def reduce(self, accumalator, event):
        pass


@pytest.fixture()
def storage():
    return Memory()


def test_stream_graph_generator(storage):
    graph = graph_generator([Filter(), Map()], storage)
    assert isinstance(graph, StreamGraph)


def test_stream_graph_repr(storage):
    graph = graph_generator([Filter(), Map()], storage)
    assert graph.__repr__() == 'StreamGraph(FilterFunction()->MapFunction())'


def test_stream_graph_iter(storage):
    graph = graph_generator([Filter(), Map()], storage)

    nodes = [node for node in graph]

    assert len(nodes) == 2
    assert nodes[0].operation.type == 'FilterFunction'
    assert nodes[1].operation.type == 'MapFunction'

    graph = graph_generator([Filter(), Map(), Map()], storage)
    nodes = [node for node in graph]

    assert len(nodes) == 3


def test_stream_graph_add_node(storage):
    graph = StreamGraph(storage)
    graph.add_node(Filter())

    assert graph.head
    assert graph.head.next is None

    graph.add_node(Map())

    assert graph.head.next


def test_stream_graph_run(storage):
    event = {'test': 'event'}
    graph = graph_generator([Map(), Filter()], storage)

    event_collection = graph.run(EventCollection(event))

    assert len(event_collection.events) == 1
    assert event_collection.events[0] == event


def test_operation_node_process():
    node = OperationNode(Map())
    event = {'test': 'event'}

    results = node.process(EventCollection(event))

    assert isinstance(results, EventCollection)
    assert results.event_collection == [event]
