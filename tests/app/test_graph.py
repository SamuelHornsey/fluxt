from streaming.app.graph import OperationNode, StreamGraph, graph_generator
from streaming.operations import FilterFunction, MapFunction


class Map(MapFunction):
    def map(self, event):
        return super().map(event)


class Filter(FilterFunction):
    def filter(self, event):
        return super().filter(event)


def test_stream_graph_generator():
    graph = graph_generator([Filter(), Map()])
    assert isinstance(graph, StreamGraph)


def test_stream_graph_repr():
    graph = graph_generator([Filter(), Map()])
    assert graph.__repr__() == 'StreamGraph(FilterFunction()->MapFunction())'


def test_stream_graph_add_node():
    graph = StreamGraph()
    graph.add_node(Filter())

    assert graph.head
    assert graph.head.next is None

    graph.add_node(Map())

    assert graph.head.next


def test_stream_graph_run():
    event = {'test': 'event'}
    graph = graph_generator([Map(), Filter()])

    graph.run(event)


def test_operation_node_process():
    node = OperationNode(Map())
    event = {'test': 'event'}

    result = node.process(event)
    assert result == event
