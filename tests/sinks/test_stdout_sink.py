from fluxt.sinks import StdoutSink

from fluxt.app.events import EventCollection


def test_stdout_sink(capsys):
    stdout = StdoutSink()
    event_collection = EventCollection({'test': 'event'})
    stdout.pipe(event_collection)
    out, err = capsys.readouterr()

    assert str(event_collection.events[0]) in out
