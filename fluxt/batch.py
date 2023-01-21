class BatchOutput:
    def __init__(self):
        self.batch = []

    def clear(self):
        self.batch = []

    def send(self, event):
        self.batch.append(event)
