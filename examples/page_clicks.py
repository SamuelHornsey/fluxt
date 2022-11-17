from streaming import App
from streaming.storage import Memory

import streaming.operations as operations

storage = Memory()
app = App(name='Page Views', storage=storage)

class FormatEvents(operations.MapFunction):
    def map(self, event):
        return self.keyed_event(event['page'], event['page_views'])

class CountViews(operations.ReducerFunction):
    def reduce(self, key, reduced, event):
        if not reduced:
            return event

        return reduced + event

@app.stream()
def views_per_page(ds):
    ds.source_from_collection([
      {'username': 'sam', 'page_views': 11, 'page': 'about'},
      {'username': 'sam', 'page_views': 7, 'page': 'home'},
      {'username': 'bill', 'page_views': 9, 'page': 'about'},
      {'username': 'reg', 'page_views': 5, 'page': 'home'},
    ])

    ds.print()

    ds.map(FormatEvents()) \
      .reduce(CountViews())