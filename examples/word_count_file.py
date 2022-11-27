import string

from fluxt.app import Fluxt

import fluxt.operations as operations

from fluxt.sources import FileSource
from fluxt.sinks import FileSink
from fluxt.storage import RocksDB

# create a streaming app
fluxt = Fluxt(name='Word Count File')

fluxt.storage = RocksDB('scratch/data')


@operations.flat_map()
def tokenizer(event):
    return event.lower().split()


@operations.map()
def remove_grammer(event):
    return event.translate(str.maketrans('', '', string.punctuation))


@operations.reducer()
def count_reducer(key, accum, event):
    if not accum:
        return str(1)
    return str(int(event) + int(accum))


@operations.key_by()
def key_index(event):
    return event, 1


@fluxt.stream()
def stream_processor(datastream):
    datastream.add_source(FileSource('examples/data/lorem_ipsum.txt'))

    datastream.pipeline(tokenizer, remove_grammer,
                        key_index, count_reducer)

    datastream.add_sink(FileSink('output.txt'))
