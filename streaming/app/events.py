class EventCollection(object):
    def __init__(self, event):
        self.event_collection = [event]

    def __bool__(self):
        if self.event_collection:
            return True
        return False

    def read_events(self):
        for event in self.event_collection:
            yield event

    @property
    def events(self):
        return self.event_collection

    @events.setter
    def events(self, events):
        self.event_collection = events