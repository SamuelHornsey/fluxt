from fluxt.sinks.base import Sink


class FileSink(Sink):
    def __init__(self, destination):
        """ init file sink """
        self.destination = destination
        self.file = open(self.destination, 'w')

    def pipe(self, batch):
        """ pipe event to file output """
        for event in batch:
            self.file.write(f'{event}\n')
