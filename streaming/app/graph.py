class GraphException(Exception):
    pass


def graph_generator(transformations):
    """ generate a stream execution graph

    Args:
        transformations (list): list of transformations
    """
    if not transformations:
        raise GraphException('no transformations defined')

    graph = StreamGraph()

    for operation in transformations:
        graph.add_node(operation)

    return graph


class StreamGraph(object):
    """ represent the streaming process graph """

    def __init__(self):
        """ init graph """
        self.head = None

    def __repr__(self):
        """ print graph """
        nodes = []
        current = self.head

        while current is not None:
            nodes.append(f'{current.operation.type}()')
            current = current.next

        return f'StreamGraph({"->".join(nodes)})'

    def add_node(self, operation):
        """ adds operation node to graph

        Args:
            operation (object): operation node
        """
        node = OperationNode(operation)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node

    def run(self, event):
        """ run graph

        Args:
            event (event): event object
        """
        current = self.head

        while current.next:
            event = current.process(event)

            if not event:
                break

            current = current.next

        return event


class OperationNode(object):
    """ represent an operation as a node """

    def __init__(self, operation):
        """ init node """
        self.operation = operation
        self.next = None

    def process(self, event):
        return self.operation(event)
