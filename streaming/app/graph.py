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

    def __iter__(self):
        """ iterator for graph nodes

        Returns:
            StreamGrapgh: stream graph self
        """
        self.current = self.head
        return self

    def __next__(self):
        """ loop through nodes

        Raises:
            StopIteration: when all nodes are listed

        Returns:
            OperationNode: operation node
        """
        while self.current is not None:
            node = self.current
            self.current = self.current.next

            return node

        raise StopIteration

    def __repr__(self):
        """ print graph """
        nodes = [f'{node.operation.type}()' for node in self]
        return f'StreamGraph({"->".join(nodes)})'

    def add_node(self, operation):
        """ adds operation node to graph

        Args:
            operation (object): operation node
        """
        new_node = OperationNode(operation)

        if not self.head:
            self.head = new_node
            return

        last = None

        for node in self:
            last = node

        last.next = new_node

    def run(self, event):
        """ run graph

        Args:
            event (event): event object
        """
        for node in self:
            event = node.process(event)

            if not event:
                break

        return event


class OperationNode(object):
    """ represent an operation as a node """

    def __init__(self, operation):
        """ init node """
        self.operation = operation
        self.next = None

    def process(self, event):
        """ run operation over event """
        return self.operation(event)
