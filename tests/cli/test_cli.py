import importlib

from fluxt import __version__
from fluxt.cli import run, about


class MockApp():
    @staticmethod
    def run():
        pass


class MockModule():
    fluxt = MockApp()
    app = MockApp()


def test_run_command(monkeypatch):
    def mock_import(module):
        return MockModule()

    monkeypatch.setattr(importlib, 'import_module', mock_import)

    run('my_test_module')
    run('my_test_module', 'app')


def test_about_command(capsys):
    about()
    out, err = capsys.readouterr()
    assert __version__ in out
