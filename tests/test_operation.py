from fluxt.operation import Operation
from fluxt.state import State


def test_operation_run():
    def my_handler(event, output, state):
        output.send(event)

    state = State('my_state', default=0, value_type=None)
    operation = Operation(my_handler, state)

    batch = operation.process_batch(['test-event'])
    assert batch == ['test-event']
