# Streamable

> A python native stateful streaming framework

> :warning: **Very Early Development**: This platform will change rapidly

## About

This is a new project that is in very early development stages. This project aims to provide a pythonic, native alternative to Spark, Flink or Storm. 

## Features

- Python native
- Multiple source/sink support
  - Kafka
  - Pulsar
  - Elasticsearch
  - JDBC
  - Files
  - Network
  - influxDB
- Stateful stream processing
- Local single node dev mode
- Multi node prod mode

## Getting Started

```python
from streaming.app import App
import streaming.operations as operations

# create a streaming app
app = App(name='Word Count')


class Tokenizer(operations.FlatMapFunction):
    def flat_map(self, event):
        return event.lower().split()


class KeyIndex(operations.MapFunction):
    def map(self, event):
        return self.keyed_event(event, 1)


class CountReducer(operations.ReducerFunction):
    def reduce(self, key, reduced, event):
        if reduced is None:
            return 1

        return reduced + event


@app.stream()
def stream_processor(datastream):
    events = ['event', 'event text', 'event test test',
              'test text event hello hello']
    print(f'input events = {events}')

    datastream.source_from_collection(events)

    datastream.flat_map(Tokenizer()) \
        .map(KeyIndex()) \
        .reduce(CountReducer())

    datastream.print()

```