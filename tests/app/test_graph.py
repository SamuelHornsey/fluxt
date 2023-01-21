import pytest

from fluxt import Fluxt
from fluxt.app.datastream import DataStream
from fluxt.app.graph import StreamGraph, GraphException, graph_generator


@pytest.fixture()
def app():
    return Fluxt('Test App')


def test_graph_generator(app):
    with pytest.raises(GraphException):
        graph = graph_generator([])

    @app.operation()
    def my_handler(event, output):
        pass

    ds = DataStream('my datastream', {})
    ds.pipeline(my_handler)

    graph = graph_generator(ds.operations)

    assert graph.num_nodes == 1

    ds.pipeline(my_handler)
    graph = graph_generator(ds.operations)

    assert graph.num_nodes == 2


def test_graph_repr(app):
    @app.operation()
    def my_handler(event, output):
        pass

    ds = DataStream('my datastream', {})
    ds.pipeline(my_handler)
    graph = graph_generator(ds.operations)

    assert graph.__repr__() == 'StreamGraph(Operation())'

    ds.pipeline(my_handler)
    graph = graph_generator(ds.operations)

    assert graph.__repr__() == 'StreamGraph(Operation()->Operation())'
