import uuid

from fluxt.sources.base import Source, NAMESPACE_FLUXT


class FileSource(Source):
    def __init__(self, file):
        """ init collection source """
        self.file = file

    def generate(self):
        """ generate events """
        with open(self.file, 'r', encoding='UTF-8') as f:
            for line in f.readlines():
                yield line.strip()

    @property
    def source_partition_key(self):
        return uuid.uuid5(NAMESPACE_FLUXT, self.file)
