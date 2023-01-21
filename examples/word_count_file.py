import string

from fluxt import Fluxt
from fluxt.sources import FileSource
from fluxt.sinks import FileSink


# create a streaming app
fluxt = Fluxt(name='Word Count File')

word_counts = fluxt.State('word_count_file', default=0)


@fluxt.operation()
def tokenizer(event, output):
    for word in event.lower().split():
        output.send(word)


@fluxt.operation()
def remove_grammer(event, output):
    output.send(event.translate(str.maketrans('', '', string.punctuation)))


@fluxt.operation(state=word_counts)
def count_reducer(event, output, state):
    state[event] += 1
    output.send((event, state[event]))


@fluxt.stream()
def stream_processor(datastream):
    datastream.add_source(FileSource('examples/data/lorem_ipsum.txt'))

    datastream.pipeline(tokenizer, remove_grammer, count_reducer)

    datastream.add_sink(FileSink('output.txt'))
