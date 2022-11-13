def graph_generator(transformations):
    """ generate a stream execution graph

    Args:
        transformations (list): list of transformations
    """
    graph = StreamGraph()

    for operation in transformations:
        graph.add_node(operation)

    return graph


class StreamGraph(object):
    """ represent the streaming process graph """

    def __init__(self):
        self.start = None

    def add_node(self, operation):
        node = OperationNode(operation)

        if not self.start:
            self.start = node


class OperationNode(object):
    """ represent an operation as a node """

    def __init__(self, operation):
        self.operation = operation
        self.next = None
