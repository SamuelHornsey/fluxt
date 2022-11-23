# fluxt

[![codecov](https://codecov.io/gh/SamuelHornsey/fluxt/branch/main/graph/badge.svg?token=NIV5LW1E98)](https://codecov.io/gh/SamuelHornsey/fluxt)
[![PyPI version](https://badge.fury.io/py/fluxt.svg)](https://badge.fury.io/py/fluxt)

A python native stateful streaming framework

## About

⚠️ **Very Early Development**: This platform will change rapidly

This is a new project that is in very early development stages. This project aims to provide a pythonic, native alternative to Spark, Flink or Storm. 

## Getting Started

```python
from fluxt import Fluxt
import fluxt.operations as operations

# create a streaming app
fluxt = Fluxt(name='Word Count')


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


@fluxt.stream()
def stream_processor(datastream):
    events = ['welcome', 'to', 'fluxt!',
                'The', 'python', 'streaming framework']

    datastream.source_from_collection(events)

    datastream.flat_map(tokenizer) \
        .key_by(key) \
        .reduce(count)

    datastream.print()


if __name__ == '__main__':
    # run the fluxt app
    fluxt.run()
```