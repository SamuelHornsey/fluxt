import pytest

from fluxt.app import Fluxt
from fluxt.operations import MapFunction
from fluxt.app.graph import GraphException


class Map(MapFunction):
    def map(self, event):
        return super().map(event)


@pytest.fixture()
def app():
    return Fluxt(name='Test Streaming App')


def test_repr(app):
    assert app.__repr__() == 'Fluxt(name="Test Streaming App")'


def test_stream(app):
    @app.stream()
    def stream(ds):
        ds.source_from_collection([1, 2, 3])
        ds.print()

    assert len(app.agents) == 1

    @app.stream()
    def stream_agent(ds):
        ds.source_from_collection([1, 2, 3])
        ds.print()

    assert len(app.agents) == 2


def test_run_no_transformations(app):
    @app.stream()
    def stream(ds):
        ds.source_from_collection([1, 2, 3])
        ds.print()

    with pytest.raises(GraphException) as e:
        app.run()

    assert 'no transformations defined' in str(e)


def test_run(app, capsys):
    @app.stream()
    def stream(ds):
        ds.source_from_collection([1, 2, 3])
        ds.print()

        ds.map(Map())

    app.run()
    out, err = capsys.readouterr()

    assert ['1', '2', '3'] == out.split()
