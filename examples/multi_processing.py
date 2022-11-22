import time

from streaming import App

import streaming.operations as operations

# create a streaming app
app = App(name='Multi Processing')

@operations.map()
def map_processor(event):
    return f'mapped-{event}'


@operations.filter()
def filter_processor(event):
    if 'event' in event:
        return True

    return False

@operations.map()
def slow_processor(event):
    return event


@app.stream()
def stream_processor(datastream):
    events = ['event1', 'event2', 'event3', 'bad']
    print(f'input events = {events}')

    datastream.source_from_collection(events)

    datastream.filter(filter_processor) \
          .map(map_processor)

    datastream.print()


@app.stream()
def other_stream_processor(datastream):
    events = ['event1-other', 'event2-other', 'event3-other', 'bad-other']
    print(f'input events = {events}')

    datastream.source_from_collection(events)

    datastream.filter(filter_processor) \
          .map(slow_processor)

    datastream.print()