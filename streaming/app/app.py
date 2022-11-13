from streaming.app.datastream import DataStream


class App(object):
    """ Streaming App Container """
    agents = []

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
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

        for agent in self.agents:
            agent(datastream)

        datastream.execute()
