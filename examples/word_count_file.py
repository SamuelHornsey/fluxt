import string

from streaming.app import App

import streaming.operations as operations

from streaming.sources import FileSource
from streaming.sinks import FileSink

# create a streaming app
app = App(name='Word Count File')

@operations.flat_map()
def tokenizer(event):
    return event.lower().split()

@operations.map()
def remove_grammer(event):
    return event.translate(str.maketrans('', '', string.punctuation))

@operations.reducer()
def count_reducer(key, accum, event):
    if not accum:
        return 1
    return event + accum


class KeyIndex(operations.MapFunction):
    def map(self, event):
        return self.keyed_event(event, 1)


@app.stream()
def stream_processor(datastream):
    datastream.add_source(FileSource('examples/data/lorem_ipsum.txt'))

    datastream.pipeline(tokenizer, remove_grammer,
                            KeyIndex(), count_reducer)

    datastream.add_sink(FileSink('output.txt'))