from streaming.sinks import FileSink

from streaming.app.events import EventCollection


def test_file_sink(monkeypatch):
    agg = []

    def mock_pipe_capture(event_collection):
        for event in event_collection.events:
            agg.append(event)

    sink = FileSink('output.txt')
    event_collection = EventCollection({'test': 'event'})
    monkeypatch.setattr(sink, 'pipe', mock_pipe_capture)

    sink.pipe(event_collection)

    assert len(agg) == len(event_collection.events)
    assert agg[0] == event_collection.events[0]
