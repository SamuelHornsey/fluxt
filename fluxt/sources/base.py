import uuid

from abc import ABC, abstractmethod, abstractproperty

NAMESPACE_FLUXT = uuid.uuid5(uuid.NAMESPACE_URL,
                             'https://github.com/SamuelHornsey/fluxt')


class Source(ABC):
    @abstractmethod
    def generate(self):
        """ generate events """
        pass

    @abstractproperty
    def source_partition_key(self):
        """ returns a unique partition key for source """
        pass
