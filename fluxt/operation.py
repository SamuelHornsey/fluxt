from fluxt.batch import BatchOutput


class Operation:
    """ operation handler class """

    def __init__(self, handler, state):
        self.handler = handler
        self.state = state

        self.output = BatchOutput()

        # next for execution graph
        self.next = None

    def process_batch(self, batch):
        """ process a micro-batch of events """
        for event in batch:
            self.run(event)

        return self.flush()

    def run(self, event):
        """ run the operation over an event """
        if self.state:
            return self.handler(event, self.output, self.state)
        return self.handler(event, self.output)

    def flush(self):
        batch = self.output.batch
        self.output.clear()
        return batch
