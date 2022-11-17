import logging

import streaming.operations as operations

from streaming.app.graph import graph_generator
from streaming.sources import CollectionSource
from streaming.sinks import StdoutSink

logger = logging.getLogger(__name__)


class DataStreamException(Exception):
    """ DataStream error """
    pass


class DataStream(object):
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

    def map(self, map_function):
        """ add mapper

        Args:
            map_function (MapFunction): mapping function class

        Returns:
            datastream (DataStream): datastream self
        """

        if not isinstance(map_function, operations.MapFunction):
            raise TypeError(f'{map_function} is '
                            f'not type {operations.MapFunction.__name__}')

        self.transformations.append(map_function)

        return self

    def filter(self, filter_function):
        """ add filter function

        Args:
            filter_function (FilterFunction): filter function

        Returns:
            datastream (DataStream): datastream self
        """
        if not isinstance(filter_function, operations.FilterFunction):
            raise TypeError(f'{filter_function} is '
                            f'not type {operations.FilterFunction.__name__}')

        self.transformations.append(filter_function)

        return self

    def flat_map(self, flat_map_function):
        """ add flat map function

        Args:
            flat_map_function (FlatMapFunction): flat map function

        Raises:
            TypeError: if function is not a flat map

        Returns:
            datastream (DataStream): datastream self
        """
        if not isinstance(flat_map_function, operations.FlatMapFunction):
            raise TypeError(f'{flat_map_function} is '
                            f'not type {operations.FlatMapFunction.__name__}')

        self.transformations.append(flat_map_function)

        return self

    def reduce(self, reduce_function):
        """ add reducer functions

        Args:
            reduce_function (ReducerFunction): reducer function

        Raises:
            TypeError: if function is not reducer

        Returns:
            datastream (DataStream): datastream self
        """
        if not isinstance(reduce_function, operations.ReducerFunction):
            raise TypeError(f'{reduce_function} is '
                            f'not type {operations.ReducerFunction.__name__}')

        self.transformations.append(reduce_function)

        return self

    def execute(self):
        """ execute datastream transformations """
        if not self.source:
            raise DataStreamException('DataStream source not defined')

        if not self.sink:
            raise DataStreamException('DataStream sink not defined')

        execution_graph = graph_generator(self.transformations, self.storage)

        for event in self.source.generate():
            data = execution_graph.run(event)
            self.sink.pipe(data)
