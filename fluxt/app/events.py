class EventCollection(object):
    """ contain the event batch being processed """

    def __init__(self, base_event):
        """ init event collection """
        self.event_collection = [base_event]

    def __bool__(self):
        """ check if event collection is populated """
        if self.event_collection:
            return True
        return False

    @property
    def events(self):
        """ return list of events """
        return self.event_collection

    @events.setter
    def events(self, events):
        """ set list of events """
        self.event_collection = events
