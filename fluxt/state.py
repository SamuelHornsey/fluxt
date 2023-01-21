import uuid
import logging

from fluxt.globals import NAMESPACE_FLUXT
from fluxt.serialization.types import get_type_encoder


logger = logging.getLogger(__name__)


class State:
    def __init__(self, name, default, value_type):
        self.state = {}

        self.name = name
        self.default = default
        self.partition_key = uuid.uuid5(NAMESPACE_FLUXT, name)
        self.type = value_type if value_type else type(default)

        if value_type:
            self.encoder = get_type_encoder(value_type)
        else:
            self.encoder = get_type_encoder(type(default))

    def __setitem__(self, key, value):
        self.transaction_log_push('set', key, value)
        self.state[key] = value

    def __getitem__(self, key):
        try:
            return self.state[key]
        except KeyError:
            return self.default

    def __delitem__(self, key):
        self.transaction_log_push('del', key)
        del self.state[key]

    def transaction_log_hook(self, transaction_log):
        self.transaction_log = transaction_log

    def transaction_log_push(self, action, key, value=None):
        self.transaction_log.append(
            action,
            key.encode('utf-8'),
            self.encoder.dumps(value),
            self.partition_key
        )

    def load_state(self, state):
        for key, value in state:
            self.state[key.decode()] = self.encoder.loads(value)
