from fluxt.operation import Operation
from fluxt.sources import CollectionSource
from fluxt.sinks import StdoutSink
from fluxt.transaction import TransactionLog
from fluxt.state import State
from fluxt.app.graph import graph_generator


class DataStreamException(Exception):
    pass


class DataStream:
    """ DataStream class """

    def __init__(self, name, store, source=None, sink=None):
        """ init DataStream """
        self.operations = []
        self.transaction_log = TransactionLog(name)

        self.name = name
        self.store = store
        self.source = source
        self.sink = sink

    def source_from_collection(self, events):
        """ create a source from collection object """
        self.source = CollectionSource(events)

    def print(self):
        """ print output to stdout """
        self.sink = StdoutSink()

    def add_source(self, source):
        """ add a source """
        self.source = source

    def add_sink(self, sink):
        """ add a sink """
        self.sink = sink

    def pipeline(self, *args):
        """ create an operation pipeline """
        for handler, state in args:
            if state and not isinstance(state, State):
                raise TypeError(f'{state} is not type {State.__name__}')

            self.transaction_log.attach(state)

            # TODO: tidy
            if state:
                state.load_state(self.store.recover_state(state.partition_key))

            self.operations.append(Operation(handler, state))

        return self

    def execute(self):
        """ execute datastream operations """
        if not self.source:
            raise DataStreamException('DataStream source not defined')

        if not self.sink:
            raise DataStreamException('DataStream sink not defined')

        execution_graph = graph_generator(self.operations)

        for event in self.source.generate():
            event_batch = execution_graph.run(event)
            self.transaction_log.commit(self.store)
            self.sink.pipe(event_batch)
