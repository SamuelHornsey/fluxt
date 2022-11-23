from fluxt.app import Fluxt
import fluxt.operations as operations

# create a streaming app
fluxt = Fluxt(name='Word Count')

@operations.flat_map()
def tokenizer(event):
    return event.lower().split(' ')

@operations.key_by()
def key_by(event):
    return (event, 1)

@operations.reducer()
def count(key, accum, event):
    if accum is None:
        return 1

    return accum + event


@fluxt.stream()
def stream_processor(datastream):
    events = ['event', 'event text', 'event test test',
              'test text event hello hello']
    print(f'input events = {events}')

    datastream.source_from_collection(events)

    datastream.pipeline(tokenizer, key_by, count)

    datastream.print()
