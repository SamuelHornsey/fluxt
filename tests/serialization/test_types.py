import pytest

import fluxt.serialization.encoders as encoders

from fluxt.serialization.types import get_type_encoder


class BadType():
    pass


def test_get_type_encoder():
    enc = get_type_encoder('str')
    assert isinstance(enc, encoders.StrEncoder)

    enc = get_type_encoder(type('str'))
    assert isinstance(enc, encoders.StrEncoder)

    with pytest.raises(encoders.EncoderError):
        get_type_encoder(type(BadType))
