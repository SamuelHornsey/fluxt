from streaming.app import App
from streaming.operations import FilterFunction, FlatMapFunction

# create a streaming app
app = App(name='Word Count')


class Tokenizer(FlatMapFunction):
    def flat_map(self, event):
        return event.lower().split()


class Filter(FilterFunction):
    def filter(self, event):
        return super().filter(event)


class WordFilter(FilterFunction):
    def filter(self, event):
        if 'event' not in event:
            return True
        return False

@app.stream()
def stream_processor(datastream):
    events = ['event', 'event text', 'event test']
    print(f'input events = {events}')

    datastream.source_from_collection(events)

    datastream.filter(Filter()) \
        .flat_map(Tokenizer()) \
        .filter(WordFilter())

    datastream.print()
