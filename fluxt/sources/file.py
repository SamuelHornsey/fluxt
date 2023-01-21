from fluxt.sources.base import Source


class FileSource(Source):
    def __init__(self, file):
        """ init collection source """
        self.file = file

    def generate(self):
        """ generate events """
        with open(self.file, 'r', encoding='UTF-8') as f:
            for line in f.readlines():
                yield line.strip()
