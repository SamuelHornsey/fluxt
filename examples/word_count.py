from streaming.app import App
from streaming.operations import MapFunction, FlatMapFunction, ReducerFunction

# create a streaming app
app = App(name='Word Count')


class Tokenizer(FlatMapFunction):
    def flat_map(self, event):
        return event.lower().split()

class KeyIndex(MapFunction):
    def map(self, event):
        return self.keyed_event(event, 1)

class CountReducer(ReducerFunction):
    def reduce(self, key, reduced, event):
        if reduced == None:
            return 1

        return reduced + event

@app.stream()
def stream_processor(datastream):
    events = ['event', 'event text', 'event test test', 'test text event hello hello']
    print(f'input events = {events}')

    datastream.source_from_collection(events)

    datastream.flat_map(Tokenizer()) \
        .map(KeyIndex()) \
        .reduce(CountReducer())

    datastream.print()
