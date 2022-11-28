class Table:
    def __init__(self, partition_key):
        self.partition_key = partition_key
        self.state = {}
        self.change_log = []

    def __setitem__(self, key, value):
        self.change_log.append(('set', key, value))
        self.state[key] = value

    def __getitem__(self, key):
        return self.state[key]

    def __delitem__(self, key):
        self.change_log.append('del', key)
        del self.state[key]

    def append_to_changelog(self, action, key, value):
        pass

    def flush_changes(self):
        pass

