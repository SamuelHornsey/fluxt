from fluxt.sources import CollectionSource


def test_collection_source():
    collection = ['1', '2', '3']
    source = CollectionSource(collection)
    assert source.collection == collection


def test_collection_source_generate():
    source = CollectionSource(['event'])

    for event in source.generate():
        assert event == 'event'
