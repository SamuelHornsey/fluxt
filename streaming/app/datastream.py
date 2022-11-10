import logging

import streaming.operations as operations

from streaming.sources import CollectionSource
from streaming.sinks import StdoutSink

logger = logging.getLogger(__name__)

class DataStream(object):
    transformations = []

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
    
    def map(self, map_function):
        """ add mapper

        Args:
            map_function (MapFunction): mapping function class

        Returns:
            DataStream: datastream self
        """

        if not isinstance(map_function, operations.MapFunction):
            raise TypeError(f'{map_function.__name__} is '
                f'not type {operations.MapFunction.__name__}')

        self.pipeline.append(map_function)

        return self
    
    def filter(self, filter_function):
        """ add filter function

        Args:
            filter_function (FilterFunction): filter function

        Returns:
            DataStream: datastream self
        """
        if not isinstance(filter_function, operations.FilterFunction):
            raise TypeError(f'{filter_function.__name__} is '
                f'not type {operations.FilterFunction.__name__}')

        self.pipeline.append(filter_function)

        return self
    
    def execute(self):
        """ execute datastream pipeline """
        for event in self.source.generate():
            data = event

            for process in self.pipeline:
                data = process(data)

            self.sink.pipe(data)