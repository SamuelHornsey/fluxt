import fluxt.serialization.encoders as encoders


TYPE_ENCODER_MAP = {
    'int': encoders.IntEncoder(),
    'str': encoders.StrEncoder(),
    'float': encoders.FloatEncoder()
}


def get_type_encoder(type_key):
    if isinstance(type_key, str) and TYPE_ENCODER_MAP.get(type_key):
        return TYPE_ENCODER_MAP[type_key]

    if isinstance(type_key, type) and TYPE_ENCODER_MAP.get(type_key.__name__):
        return TYPE_ENCODER_MAP[type_key.__name__]

    raise encoders.EncoderError(
        f'no available encoder for type {type_key}')
