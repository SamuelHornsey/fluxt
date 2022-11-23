from fluxt import Fluxt
from fluxt.storage import Memory

import fluxt.operations as operations

storage = Memory()

fluxt = Fluxt(name='Page Views', storage=storage)

class FormatEvents(operations.MapFunction):
    def map(self, event):
        return event['page'], event['page_views']

class CountViews(operations.ReducerFunction):
    def reduce(self, key, reduced, event):
        if not reduced:
            return event

        return reduced + event

@operations.key_by()
def key(event):
    return event[0], event[1]

@fluxt.stream()
def views_per_page(ds):
    ds.source_from_collection([
      {'username': 'sam', 'page_views': 11, 'page': 'about'},
      {'username': 'sam', 'page_views': 7, 'page': 'home'},
      {'username': 'bill', 'page_views': 9, 'page': 'about'},
      {'username': 'reg', 'page_views': 5, 'page': 'home'},
    ])

    ds.print()

    ds.map(FormatEvents()) \
      .key_by(key) \
      .reduce(CountViews())