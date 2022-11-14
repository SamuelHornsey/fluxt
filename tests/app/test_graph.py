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


def test_stream_graph_iter():
    graph = graph_generator([Filter(), Map()])

    nodes = [node for node in graph]

    assert len(nodes) == 2
    assert nodes[0].operation.type == 'FilterFunction'
    assert nodes[1].operation.type == 'MapFunction'

    graph = graph_generator([Filter(), Map(), Map()])
    nodes = [node for node in graph]

    assert len(nodes) == 3


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

    processed_event = graph.run(event)

    assert processed_event == event


def test_operation_node_process():
    node = OperationNode(Map())
    event = {'test': 'event'}

    result = node.process(event)
    assert result == event
