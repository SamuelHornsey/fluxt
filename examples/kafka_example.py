from streaming.app import App
from streaming.operations import MapFunction, FilterFunction
from streaming.sources import KafkaSource

# create a streaming app
app = App(name='My Kafka Stream Processor')

class MapProcessor(MapFunction):
    def map(self, event):
        return f'mapped-{event}'

class FilterProcessor(FilterFunction):
    def filter(self, event):
        if 'event' in event:
            return True

        return False

@app.stream()
def stream_processor(data_stream):
    data_stream.add_source(KafkaSource('foobar', bootstrap_servers='127.0.0.1:9092'))

    map_p = MapProcessor()
    filter_p = FilterProcessor()

    data_stream.filter(filter_p) \
          .map(map_p)

    data_stream.print()