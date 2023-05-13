from base64 import b64decode
from hashlib import md5
from password_crypt import password_decrypt
from json import loads
from generate_key import generate_key


def _check_sign(message: str, sign: str) -> str:
    return md5(message.encode('utf-8')).hexdigest() == sign


def decode_key(message: str, key: str) -> str:
    message, sign = b64decode(message).decode().split('.')
    assert _check_sign(message, sign), 'Подпись не совпадает'
    message = password_decrypt(message, key)
    return loads(message)


def read_file(path: str, serial_number: str) -> dict:
    with open(path) as f:
        message = f.readline()
    key = generate_key(serial_number)
    return decode_key(message, key)
