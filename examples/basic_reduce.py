import logging

from fluxt import Fluxt

# setting logging level to debug
logging.basicConfig(level=logging.DEBUG)

# create a streaming app
fluxt = Fluxt(name='basic_reduce', datadir='/tmp/data')

word_count = fluxt.State('word_count', default=0)


@fluxt.operation()
def tokenize(event, output):
    for word in event.lower().split():
        output.send(word)


@fluxt.operation(state=word_count)
def count(event, output, state):
    state[event] += 1
    output.send((event, state[event]))


@fluxt.stream()
def word_count_processor(datastream):
    events = ['event', 'event text', 'event test test',
              'test text event hello hello']
    print(f'input events = {events}')

    datastream.source_from_collection(events)

    datastream.pipeline(tokenize, count)

    datastream.print()
