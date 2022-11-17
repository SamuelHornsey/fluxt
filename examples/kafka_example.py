from streaming.app import App
from streaming.operations import MapFunction, FilterFunction, FlatMapFunction, ReducerFunction
from streaming.sources import KafkaSource

# create a streaming app
app = App(name='My Kafka Stream Processor')

class MapProcessor(MapFunction):
    def map(self, event):
        return self.keyed_event(event, 1)

class FilterProcessor(FilterFunction):
    def filter(self, event):
        if 'badstring' in event:
            return False

        return True

class FlatMapProcessor(FlatMapFunction):
    def flat_map(self, event):
        return event.upper().split(' ')

class WordCount(ReducerFunction):
    def reduce(self, key, reduced, event):
        if not reduced:
            return event

        return reduced + event

@app.stream()
def stream_processor(data_stream):
    data_stream.add_source(KafkaSource('foobar', bootstrap_servers='localhost:9092'))

    data_stream.filter(FilterProcessor()) \
                .flat_map(FlatMapProcessor()) \
                .map(MapProcessor()) \
                .reduce(WordCount())

    data_stream.print()
