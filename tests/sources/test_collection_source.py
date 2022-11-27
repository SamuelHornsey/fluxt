import uuid

from fluxt.sources.base import NAMESPACE_FLUXT
from fluxt.sources import CollectionSource


def test_collection_source():
    collection = ['1', '2', '3']
    source = CollectionSource(collection)
    assert source.collection == collection


def test_collection_source_generate():
    source = CollectionSource(['event'])

    for event in source.generate():
        assert event == 'event'


def test_collection_source_partition_key():
    source = CollectionSource(['event'])

    partition_key = source.source_partition_key

    assert partition_key == uuid.uuid5(NAMESPACE_FLUXT, str(['event']))
