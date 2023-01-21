import logging

from fluxt import Fluxt

# setting logging level to debug
logging.basicConfig(level=logging.DEBUG)

# create a streaming app
fluxt = Fluxt(name='My Stream Processor')


@fluxt.operation()
def map_events(event, output):
    output.send(f'mapped-{event}')


@fluxt.operation()
def filter_events(event, output):
    if 'event' in event:
        output.send(event)


@fluxt.stream()
def stream_processor(datastream):
    events = ['event1', 'event2', 'event3', 'bad']
    print(f'input events = {events}')

    datastream.source_from_collection(events)

    datastream.pipeline(filter_events, map_events)

    datastream.print()
