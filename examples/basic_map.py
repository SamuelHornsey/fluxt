from fluxt import App

import fluxt.operations as operations

# create a streaming app
app = App(name='My Stream Processor')

@operations.map()
def map_processor(event):
    return f'mapped-{event}'


@operations.filter()
def filter_processor(event):
    if 'event' in event:
        return True

    return False


@app.stream()
def stream_processor(datastream):
    events = ['event1', 'event2', 'event3', 'bad']
    print(f'input events = {events}')

    datastream.source_from_collection(events)

    datastream.filter(filter_processor) \
          .map(map_processor)

    datastream.print()