import pytest

from fluxt import Fluxt
from fluxt.state import State


@pytest.fixture()
def app():
    return Fluxt(name='Test Streaming App')


def test_repr(app):
    assert app.__repr__() == 'Fluxt(name="Test Streaming App")'


def test_state(app):
    state = app.State('my_state', default=0)

    assert isinstance(state, State)


def test_operation(app):
    @app.operation()
    def my_handler(event, output):
        pass

    assert isinstance(my_handler, tuple)
    assert my_handler[1] is None

    state = app.State('test_state', default=0)

    @app.operation(state=state)
    def my_handler(event, output, state):
        pass

    assert isinstance(my_handler, tuple)
    assert my_handler[1] == state


def test_stream(app):
    @app.stream()
    def stream(ds):
        pass

    assert len(app.stream_processors) == 1
    assert isinstance(app.stream_processors[0], tuple)


def test_run(app, capsys):
    @app.operation()
    def null_operation(event, output):
        output.send(event)

    @app.stream()
    def stream(ds):
        ds.source_from_collection(['test'])
        ds.pipeline(null_operation)
        ds.print()

    app.run()
    out, err = capsys.readouterr()

    assert 'test' in out.split()
