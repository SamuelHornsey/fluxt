from streaming.app import App
import streaming.operations as operations

# create a streaming app
app = App(name='Word Count')


class Tokenizer(operations.FlatMapFunction):
    def flat_map(self, event):
        return event.lower().split()


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
    events = ['event', 'event text', 'event test test',
              'test text event hello hello']
    print(f'input events = {events}')

    datastream.source_from_collection(events)

    datastream.flat_map(Tokenizer()) \
        .map(KeyIndex()) \
        .reduce(CountReducer())

    datastream.print()
