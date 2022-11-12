import pytest

from streaming.app import App

@pytest.fixture()
def app():
    return App(name='Test Streaming App')

def test_repr(app):
    assert app.__repr__() == 'App(name="Test Streaming App")'

def test_stream(app):
    @app.stream()
    def stream(ds):
        ds.source_from_collection([1,2,3])
        ds.print()
    
    assert len(app.agents) == 1
  
def test_run(app):
    @app.stream()
    def stream(ds):
        ds.source_from_collection([1,2,3])
        ds.print()
    
    app.run()