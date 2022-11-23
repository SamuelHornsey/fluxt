from fluxt.app import Fluxt
import fluxt.operations as operations
from fluxt.sources import KafkaSource

# create a streaming app
fluxt = Fluxt(name='My Kafka Stream Processor')

@operations.filter()
def filter_strings(event):
    if 'badstring'.upper() in event:
        return False
    return True

@operations.key_by()
def key(event):
    return event, 1

@operations.flat_map()
def tokenize(event):
    return event.upper().split()

@operations.reducer()
def count(key, accum, event):
    if not accum:
        return event
    return accum + event

@fluxt.stream()
def stream_processor(data_stream):
    data_stream.add_source(KafkaSource('foobar', bootstrap_servers='localhost:9092'))

    data_stream.flat_map(tokenize) \
              .filter(filter_strings) \
              .key_by(key) \
              .reduce(count)

    data_stream.print()
