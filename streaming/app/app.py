from streaming.storage import Memory
from streaming.app.datastream import DataStream


class App(object):
    """ Streaming App Container """
    agents = []

    def __init__(self, name=None, storage=None):
        """ init streaming app """
        self.name = name

        if not storage:
            storage = Memory()

        self.storage = storage

    def __repr__(self):
        """ streaming app repr """
        return f'App(name="{self.name}")'

    def stream(self, *args, **kwargs):
        """ add stream agent """
        def inner(func):
            self.agents.append(func)
            return func
        return inner

    def run(self):
        """ run streaming app """
        datastream = DataStream()

        datastream.storage = self.storage

        for agent in self.agents:
            agent(datastream)

        datastream.execute()
