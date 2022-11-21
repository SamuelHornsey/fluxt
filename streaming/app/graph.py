class GraphException(Exception):
    pass


def graph_generator(transformations, storage):
    """ generate a stream execution graph

    Args:
        transformations (list): list of transformations

    Returns:
        graph (StreamGraph): a streaming graph pipeline
    """
    if not transformations:
        raise GraphException('no transformations defined')

    graph = StreamGraph(storage)

    for operation in transformations:
        graph.add_node(operation)

    return graph


class StreamGraph(object):
    """ represent the streaming process graph """

    def __init__(self, storage):
        """ init graph """
        self.head = None
        self.storage = storage

    def __iter__(self):
        """ iterator for graph nodes

        Returns:
            self (StreamGraph): stream graph self
        """
        self.current = self.head
        return self

    def __next__(self):
        """ loop through nodes

        Raises:
            StopIteration: when all nodes are listed

        Returns:
            node (OperationNode): operation node
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

        # set storage backend
        new_node.operation.storage = self.storage

        if not self.head:
            self.head = new_node
            return

        last = None

        for node in self:
            last = node

        if new_node.operation.type == 'ReducerFunction' \
                and last.operation.type != 'KeyByFunction':
            raise GraphException(f'{new_node.operation.type} must be '
                                 'preceeded by a KeyByFunction node')

        last.next = new_node

    def run(self, event_collection):
        """ run graph by looping through each node and
            processing the event collection

        Args:
            event (event): event object
        """
        for node in self:
            event_collection = node.process(event_collection)

            if not event_collection:
                break

        return event_collection


class OperationNode(object):
    """ represent an operation as a node """

    def __init__(self, operation):
        """ init node """
        self.operation = operation
        self.next = None

    def process(self, event_collection):
        """ run operation over event """
        return self.operation(event_collection)
