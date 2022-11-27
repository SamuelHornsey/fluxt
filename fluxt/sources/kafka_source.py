import uuid

from kafka import KafkaConsumer

from fluxt.sources.base import Source, NAMESPACE_FLUXT


class KafkaSource(Source):
    def __init__(self, topic, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic

        self.consumer = KafkaConsumer(self.topic,
                                      bootstrap_servers=self.bootstrap_servers)

    def generate(self):
        for event in self.consumer:
            yield event.value.decode('utf-8')

    @property
    def source_partition_key(self):
        return uuid.uuid5(NAMESPACE_FLUXT,
                          f'{self.topic}/{self.bootstrap_servers}')
