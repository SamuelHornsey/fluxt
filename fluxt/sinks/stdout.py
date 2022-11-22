import sys

from fluxt.sinks.base import Sink


class StdoutSink(Sink):
    def pipe(self, event_collection):
        """ send event to stdout """
        for event in event_collection.events:
            sys.stdout.write('%s\n' % str(event))
