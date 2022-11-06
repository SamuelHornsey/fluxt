from streaming.app import App

# create a streaming app
app = App(name='My Stream Processor')

def mapping_processor(event):
    return f'event-{event}'

@app.stream()
def stream_processor(data_stream):
    data_stream.source_from_collection(['event1', 'event2', 'event3'])

    data_stream.map(mapping_processor).map(mapping_processor)

    data_stream.print()