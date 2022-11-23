# fluxt

> A python native stateful streaming framework

## About

> :warning: **Very Early Development**: This platform will change rapidly

This is a new project that is in very early development stages. This project aims to provide a pythonic, native alternative to Spark, Flink or Storm. 

## Getting Started

```python
from fluxt import Fluxt
import fluxt.operations as operations

# create a streaming app
app = Fluxt(name='Word Count')


@operations.flat_map()
def tokenizer(event):
    return event.lower().split()


@operations.key_by()
def key(event):
    return event, 1


@operations.reducer()
def count(key, reduced, event):
    if reduced is None:
        return 1
    return reduced + event


@app.stream()
def stream_processor(datastream):
    events = ['event', 'event text', 'event test test',
              'test text event hello hello']
    print(f'input events = {events}')

    datastream.source_from_collection(events)

    datastream.flat_map(tokenizer) \
        .key_by(key) \
        .reduce(count)

    datastream.print()

```