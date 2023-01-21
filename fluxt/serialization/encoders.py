from abc import ABC, abstractmethod


class EncoderError(Exception):
    pass


class BaseEncoder(ABC):
    @abstractmethod
    def _dumps(self, data):
        pass

    @abstractmethod
    def _loads(self, raw):
        pass

    @abstractmethod
    def validate(self, data):
        pass

    def dumps(self, data):
        self.validate(data)
        return self._dumps(data)

    def loads(self, raw):
        data = self._loads(raw)
        self.validate(data)
        return data


class IntEncoder(BaseEncoder):
    def _dumps(self, data):
        return str(data).encode('utf-8')

    def _loads(self, raw):
        return int(raw.decode())

    def validate(self, data):
        if not isinstance(data, int):
            raise EncoderError(f'{type(data)} is not int')


class StrEncoder(BaseEncoder):
    def _dumps(self, data):
        return data.encode('utf-8')

    def _loads(self, raw):
        return str(raw.decode())

    def validate(self, data):
        if not isinstance(data, str):
            raise EncoderError(f'{type(data)} is not str')


class FloatEncoder(BaseEncoder):
    def _dumps(self, data):
        return str(data).encode('utf-8')

    def _loads(self, raw):
        return float(raw.decode())

    def validate(self, data):
        if not isinstance(data, float):
            raise EncoderError(f'{type(data)} is not float')
