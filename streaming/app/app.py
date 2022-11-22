from streaming.storage import Memory
from streaming.app.datastream import DataStream

from multiprocessing import Process


class App(object):
    """ Streaming App Container """

    def __init__(self, name=None, storage=None):
        """ init streaming app """
        self.name = name
        self.agents = []

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
        streams = []
        proc = []

        for agent in self.agents:
            datastream = DataStream()
            datastream.storage = self.storage

            agent(datastream)
            streams.append(datastream)

        for stream in streams:
            process = Process(target=stream.execute)
            process.start()
            proc.append(process)


        for p in proc:
            p.join()

        # for agent in self.agents:
        #     agent(datastream)

        # datastream.execute()
