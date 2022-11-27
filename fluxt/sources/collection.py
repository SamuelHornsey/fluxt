import uuid

from fluxt.sources.base import Source, NAMESPACE_FLUXT


class CollectionSource(Source):
    def __init__(self, collection):
        """ init collection source """
        self.collection = collection

    def generate(self):
        """ generate events """
        for event in self.collection:
            yield event

    @property
    def source_partition_key(self):
        return uuid.uuid5(NAMESPACE_FLUXT,
                          str(self.collection))
