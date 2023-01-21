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
from fluxt.storage import LevelStore


# create a streaming app
fluxt = Fluxt(name='basic_reduce')

word_count = fluxt.State('word_count', default=0,
                store=LevelStore('/tmp/data'))


@fluxt.operation()
def tokenize(event, output):
    for word in event.lower().split():
        output.send(word)


@fluxt.operation(state=word_count)
def count(event, output, state):
    state[event] += 1
    output.send((event, state[event]))


@fluxt.stream()
def word_count_processor(datastream):
    events = ['welcome', 'to', 'fluxt!',
                'The', 'python', 'streaming framework']

    datastream.source_from_collection(events)

    datastream.pipeline(tokenize, count)

    datastream.print()


if __name__ == '__main__':
    # run the fluxt app
    fluxt.run()
```

### Installing Plyvel on Mac

```sh
CFLAGS='-g -stdlib=libc++ -std=c++11 -fno-rtti' pip install --force-reinstall --global-option="build_ext" --global-option="-I/usr/local/include" --global-option="-L/usr/local/lib" plyvel
```
