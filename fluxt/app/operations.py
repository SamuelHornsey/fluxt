import fluxt.operations as operations

from fluxt.operations.base import Operation


class DataStreamOperations:
    def pipeline(self, *args):
        """ create an operation pipeline """
        for operation in args:
            if not isinstance(operation, Operation):
                raise TypeError(f'{operation} is '
                                f'not type {Operation.__name__}')

            self.transformations.append(operation)

        return self

    def key_by(self, key_by_function):
        """ add key by

        Args:
            key_by_function (KeyByFunction): key by function

        Raises:
            TypeError: if functions is not type key by

        Returns:
            datastream (DataStream): datastream self
        """
        if not isinstance(key_by_function, operations.KeyByFunction):
            raise TypeError(f'{key_by_function} is '
                            f'not type {operations.KeyByFunction.__name__}')

        self.transformations.append(key_by_function)

        return self

    def map(self, map_function):
        """ add mapper

        Args:
            map_function (MapFunction): mapping function class

        Returns:
            datastream (DataStream): datastream self
        """

        if not isinstance(map_function, operations.MapFunction):
            raise TypeError(f'{map_function} is '
                            f'not type {operations.MapFunction.__name__}')

        self.transformations.append(map_function)

        return self

    def filter(self, filter_function):
        """ add filter function

        Args:
            filter_function (FilterFunction): filter function

        Returns:
            datastream (DataStream): datastream self
        """
        if not isinstance(filter_function, operations.FilterFunction):
            raise TypeError(f'{filter_function} is '
                            f'not type {operations.FilterFunction.__name__}')

        self.transformations.append(filter_function)

        return self

    def flat_map(self, flat_map_function):
        """ add flat map function

        Args:
            flat_map_function (FlatMapFunction): flat map function

        Raises:
            TypeError: if function is not a flat map

        Returns:
            datastream (DataStream): datastream self
        """
        if not isinstance(flat_map_function, operations.FlatMapFunction):
            raise TypeError(f'{flat_map_function} is '
                            f'not type {operations.FlatMapFunction.__name__}')

        self.transformations.append(flat_map_function)

        return self

    def reduce(self, reduce_function):
        """ add reducer functions

        Args:
            reduce_function (ReducerFunction): reducer function

        Raises:
            TypeError: if function is not reducer

        Returns:
            datastream (DataStream): datastream self
        """
        if not isinstance(reduce_function, operations.ReducerFunction):
            raise TypeError(f'{reduce_function} is '
                            f'not type {operations.ReducerFunction.__name__}')

        self.transformations.append(reduce_function)

        return self
