import pytest

from streaming.app import App

@pytest.fixture()
def app():
    return App(name='Test Streaming App')

def test_repr(app):
    assert app.__repr__() == 'App(name="Test Streaming App")'

def test_stream(app):
    @app.stream()
    def stream(event):
        pass
  