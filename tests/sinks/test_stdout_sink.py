from streaming.sinks import StdoutSink

def test_stdout_sink(capsys):
    stdout = StdoutSink()
    event = {'test': 'event'}
    stdout.pipe(event)
    out, err = capsys.readouterr()
    
    assert str(event) in out