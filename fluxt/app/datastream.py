import logging

from fluxt.app.operations import DataStreamOperations
from fluxt.app.events import EventCollection
from fluxt.app.graph import graph_generator
from fluxt.sources import CollectionSource
from fluxt.sinks import StdoutSink

logger = logging.getLogger(__name__)


class DataStreamException(Exception):
    """ DataStream error """
    pass


class DataStream(DataStreamOperations):
    def __init__(self, source=None, sink=None, storage=None):
        """ DataStream class

        Args:
            source (Source, optional): datastream source. Defaults to None.
            sink (Sink, optional): datastream sink. Defaults to None.
        """
        self.transformations = []
        self.source = source
        self.sink = sink
        self.storage = storage

    def source_from_collection(self, collection):
        """ source from collection type """
        self.source = CollectionSource(collection)

    def print(self):
        """ sink to stdout """
        self.sink = StdoutSink()

    def add_source(self, source):
        """ add new source for ds

        Args:
            source (Source): datastream source
        """
        self.source = source

    def add_sink(self, sink):
        """ add new sink for ds

        Args:
            sink (Sink): datastream sink
        """
        self.sink = sink

    def execute(self):
        """ execute datastream transformations """
        if not self.source:
            raise DataStreamException('DataStream source not defined')

        if not self.sink:
            raise DataStreamException('DataStream sink not defined')

        execution_graph = graph_generator(self.transformations, self.storage)

        for event in self.source.generate():
            event_collection = execution_graph.run(EventCollection(event))
            self.sink.pipe(event_collection)
