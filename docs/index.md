# Welcome to Fluxt!

Fluxt is a python native stateful streaming framework.

Inspired by larger frameworks such as Apache Flink, Spark and Apache Storm. **Fluxt** aims to implement the high performance stateful stream processors in python.

Unlike the Flink python api ([pyflink](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/python/overview/)), fluxt runs entirely in python. Meaning it plays well with all other python modules. Fluxt requires python>=3.7 to run.

## Installation

Install the latest version of fluxt with pip

```sh
pip install fluxt
```

Each fluxt connector will use optional dependencies, to install with a specific connector use the optional install syntax.

```sh
pip install fluxt[kafka]
```

## Getting Started

Here is a basic streaming mapping job example;

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

Alternatively to running the python script, fluxt apps can also be run through the cli.

```sh
fluxt run module_name --app my_fluxt_app
```