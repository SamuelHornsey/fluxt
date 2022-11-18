import string

from streaming.app import App
import streaming.operations as operations

from streaming.sources import FileSource

# create a streaming app
app = App(name='Word Count File')


class Tokenizer(operations.FlatMapFunction):
    def flat_map(self, event):
        return event.lower().split()

class RemoveGrammer(operations.MapFunction):
    def map(self, event):
        return event.translate(str.maketrans('', '', string.punctuation))


class KeyIndex(operations.MapFunction):
    def map(self, event):
        return self.keyed_event(event, 1)


class CountReducer(operations.ReducerFunction):
    def reduce(self, key, reduced, event):
        if reduced is None:
            return 1

        return reduced + event


@app.stream()
def stream_processor(datastream):
    datastream.add_source(FileSource('examples/data/lorem_ipsum.txt'))

    datastream.pipeline(Tokenizer(), RemoveGrammer(),
                            KeyIndex(), CountReducer())

    datastream.print()
