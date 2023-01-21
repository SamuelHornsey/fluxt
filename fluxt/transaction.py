import logging
import uuid
import time

from fluxt.globals import NAMESPACE_FLUXT

logger = logging.getLogger(__name__)


class TransactionLogEntry:
    def __init__(self, action, key, value, partition):
        self.action = action
        self.key = key
        self.value = value
        self.partition = partition
        self.timestamp = time.time()

    def __repr__(self):
        return f'TransactionLogEntry(key={self.key}, value={self.value})'

    def get(self):
        return self.action, self.key, self.value, self.partition


class TransactionLog:
    def __init__(self, name):
        self.log = []
        self.name = name
        self.id = uuid.uuid5(NAMESPACE_FLUXT, name)

    def append(self, action, key, value, partition):
        self.log.append(TransactionLogEntry(
            action,
            key,
            value,
            partition
        ))

    def attach(self, state):
        if not state:
            return

        state.transaction_log_hook(self)

    def commit(self, store):
        logger.debug(f'committing to store: {self.log}')
        store.apply_change_log(self.log)
        self.clear()

    def recover(self, store):
        return store.recover_state(self.partition_key)

    def clear(self):
        self.log = []
