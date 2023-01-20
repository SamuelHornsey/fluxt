import sys

from fluxt.sinks.base import Sink


class StdoutSink(Sink):
    def pipe(self, batch):
        """ send event to stdout """
        for event in batch:
            sys.stdout.write('%s\n' % str(event))
