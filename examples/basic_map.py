from streaming.app import App
from streaming.operations import MapFunction, FilterFunction

# create a streaming app
app = App(name='My Stream Processor')

class MapProcessor(MapFunction):
    def map(self, event):
        return f'mapped-{event}'

class FilterProcessor(FilterFunction):
    def filter(self, event):
        if 'event' in event:
            return event
    
        return None

@app.stream()
def stream_processor(data_stream):
    data_stream.source_from_collection(['event1', 'event2', 'event3', 'bad'])

    map_p = MapProcessor()
    filter_p = FilterProcessor()

    data_stream.filter(filter_p) \
          .map(map_p)

    data_stream.print()