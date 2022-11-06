from streaming.sources.base import Source

class CollectionSource(Source):
    def __init__(self, collection):
        self.collection = collection

    def generate(self):
        for event in self.collection:
            yield event