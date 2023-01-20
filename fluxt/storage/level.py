import plyvel

from fluxt.storage.base import BaseStorage, StorageException


class LevelStore(BaseStorage):
    def __init__(self, dir, **extra_options):
        self.partitions = {}

        if 'create_if_missing' in extra_options.keys() and \
                extra_options['create_if_missing'] is False:
            raise StorageException('LevelDB cannot be initialized with '
                                   'setting create_if_missing=False')

        extra_options['create_if_missing'] = True

        self.db = plyvel.DB(dir, **extra_options)

    def apply_change_log(self, changelog):
        for event in changelog:
            action, key, value, partition = event.get()
            db = self.get_db_partition(partition)

            if action == 'set':
                db.put(key, value)
            else:
                db.delete(key)

    def get_db_partition(self, partition_key):
        partition_key_encoded = f'{partition_key}-'.encode('utf-8')

        try:
            return self.partitions[partition_key]
        except KeyError:
            self.partitions[partition_key] = self.db \
                .prefixed_db(partition_key_encoded)
        return self.partitions[partition_key]

    def recover_state(self, partition):
        db = self.get_db_partition(partition)

        for key, value in db:
            yield key, value
