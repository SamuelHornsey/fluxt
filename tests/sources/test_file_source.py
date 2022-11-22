from fluxt.sources import FileSource


def test_file_source():
    file_path = 'examples/data/lorem_ipsum.txt'
    source = FileSource(file_path)
    assert source.file == file_path


def test_collection_source_generate():
    file_path = 'examples/data/lorem_ipsum.txt'
    source = FileSource(file_path)

    f = open(file_path)

    lines = f.readlines()
    events = []

    for event in source.generate():
        events.append(event)

    assert len(lines) == len(events)

    for i in range(len(lines)):
        assert lines[i].strip() == events[i]
