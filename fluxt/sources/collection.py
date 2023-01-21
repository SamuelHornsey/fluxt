from fluxt.sources.base import Source


class CollectionSource(Source):
    def __init__(self, collection):
        """ init collection source """
        self.collection = collection

    def generate(self):
        """ generate events """
        for event in self.collection:
            yield event
