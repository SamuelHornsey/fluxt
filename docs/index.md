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

import fluxt.operations as operations

fluxt = Fluxt()

@operations.map()
def map_event(event):
    return f'my-fluxt-event-{event}'

@fluxt.stream()
def stream_processor(datastream):
    # set some events
    events = ['event1', 'event2', 'event3']

    # add events from source
    datastream.source_from_collection(events)

    # create a pipeline
    datastream.pipeline(map_event)

    # output results to stdout
    datastream.print()

if __name__ == '__main__':
    fluxt.run()
```

Alternatively to running the python script, fluxt apps can also be run through the cli.

```sh
fluxt run module:app
```