from fluxt.sinks import FileSink

from fluxt.app.events import EventCollection


def test_file_sink(monkeypatch):
    agg = []

    def mock_file_write(event):
        agg.append(event)

    sink = FileSink('output.txt')
    event_collection = EventCollection({'test': 'event'})
    monkeypatch.setattr(sink.file, 'write', mock_file_write)

    sink.pipe(event_collection)

    assert len(agg) == len(event_collection.events)
