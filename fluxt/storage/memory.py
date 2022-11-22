from fluxt.storage.base import Base


class Memory(Base):
    def __init__(self):
        """ init memory storage """
        self.state = {}

    def reset(self):
        """ reset memory """
        self.state = {}

    def set_key(self, key, value):
        """ set key value """
        self.state[key] = value

    def get_key(self, key):
        """ get key value """
        return self.state[key]
