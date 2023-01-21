import pytest

import fluxt.serialization.encoders as encoders


def test_int_encoder():
    enc = encoders.IntEncoder()

    raw = enc.dumps(1)
    assert raw == str(1).encode('utf-8')

    data = enc.loads(raw)
    assert data == 1

    with pytest.raises(encoders.EncoderError):
        enc.dumps('test')


def test_str_encoder():
    enc = encoders.StrEncoder()

    raw = enc.dumps('test')
    assert raw == 'test'.encode('utf-8')

    data = enc.loads(raw)
    assert data == 'test'

    with pytest.raises(encoders.EncoderError):
        enc.dumps(1)


def test_float_encoder():
    enc = encoders.FloatEncoder()

    raw = enc.dumps(1.4455566)
    assert raw == str(1.4455566).encode('utf-8')

    data = enc.loads(raw)
    assert data == 1.4455566

    with pytest.raises(encoders.EncoderError):
        enc.dumps('test')
