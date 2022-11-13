import pytest

from streaming.app.graph import graph_generator, StreamGraph, OperationNode
from streaming.operations import FilterFunction, MapFunction

# test operations


class Map(MapFunction):
    def map(self, event):
        return super().map(event)


class Filter(FilterFunction):
    def filter(self, event):
        return super().filter(event)


def test_graph_generator():
    graph = graph_generator([Filter(), Map()])

    assert isinstance(graph, StreamGraph)


def test_stream_graph_add_node():
    graph = StreamGraph()
    graph.add_node(1)
