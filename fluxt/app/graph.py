class GraphException(Exception):
    pass


def graph_generator(transformations):
    """ generate a stream execution graph

    Args:
        transformations (list): list of transformations

    Returns:
        graph (StreamGraph): a streaming graph pipeline
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
        self.num_nodes = 0

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
        nodes = [f'{node.__class__.__name__}()' for node in self]
        return f'StreamGraph({"->".join(nodes)})'

    def add_node(self, operation):
        """ adds operation node to graph

        Args:
            operation (object): operation node
        """
        self.num_nodes = self.num_nodes + 1

        if not self.head:
            self.head = operation
            return

        last = None

        for node in self:
            last = node

        last.next = operation

    def run(self, event):
        """ run graph by looping through each node and
            processing the event collection

        Args:
            event (event): event object
        """
        batch = [event]
        for node in self:
            batch = node.process_batch(batch)

            if not batch:
                break

        return batch
