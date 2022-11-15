from streaming.sinks import StdoutSink


def test_stdout_sink(capsys):
    stdout = StdoutSink()
    event_collection = [{'test': 'event'}]
    stdout.pipe(event_collection)
    out, err = capsys.readouterr()

    assert str(event_collection[0]) in out
