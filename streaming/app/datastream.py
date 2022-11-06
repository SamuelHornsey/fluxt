import logging

from streaming.sources import CollectionSource
from streaming.sinks import StdoutSink

logger = logging.getLogger(__name__)

class DataStream(object):
    pipeline = []

    def __init__(self, source=None, sink=None):
        """ DataStream class

        Args:
            source (Source, optional): datastream source. Defaults to None.
            sink (Sink, optional): datastream sink. Defaults to None.
        """
        self.source = source
        self.sink = sink
    
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
    
    def map(self, func):
        """ add mapper

        Args:
            func (function): mapping function

        Returns:
            DataStream: datastream self
        """
        self.pipeline.append(func)
        return self
    
    def execute(self):
        """ execute datastream pipeline """
        for event in self.source.generate():
            data = event

            for process in self.pipeline:
                data = process(data)

            self.sink.pipe(data)