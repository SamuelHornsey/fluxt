import sys

from streaming.sinks.base import Sink

class StdoutSink(Sink):
    def pipe(self, event):
        sys.stdout.write('%s\n' % event)