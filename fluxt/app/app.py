from fluxt.state import State
from fluxt.storage import LevelStore

from fluxt.app.datastream import DataStream


class Fluxt:
    """ Fluxt application """

    def __init__(self, name=None, datadir='/tmp'):
        """ init fluxt """
        self.name = name
        self.stream_processors = []
        self.datadir = datadir
        self.store = LevelStore(self.datadir)

    def __repr__(self):
        """ print(fluxt) """
        return f'Fluxt(name="{self.name}")'

    def State(self, name, default=None, value_type=None):
        """ returns state fluxt object """
        return State(name, default, value_type)

    def operation(self, *args, **kwargs):
        """ wrap operation handler """
        def inner(func):
            state = kwargs.get('state', None)
            return func, state
        return inner

    def stream(self, *args, **kwargs):
        """ add stream processor """
        def inner(func):
            procssor_name = kwargs.get('name', func.__name__)
            self.stream_processors.append((procssor_name, func))
            return func
        return inner

    def run(self):
        """ run streaming app """
        for name, processor in self.stream_processors:
            datastream = DataStream(name, self.store)
            processor(datastream)

        datastream.execute()
