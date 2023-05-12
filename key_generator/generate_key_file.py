from datetime import datetime
from password_crypt import password_encrypt
from json import dumps
from base64 import b64encode
from hashlib import md5
from generate_key import generate_key


def _generate_unencrypted_key(owner: str, lifetime: int, level: int) -> str:
    return dumps(
        {
            'owner': owner,
            'date_creation': str(datetime.now()),
            'lifetime': lifetime,
            'level': level,
        },
        ensure_ascii=False,
    )


def _sign_key(message: str) -> str:
    sign = md5(message.encode('utf-8')).hexdigest()
    message = (message + '.' + sign).encode()
    return b64encode(message).decode()


def _generate_crypted_key(owner: str, lifetime: int, level: int, key: str) -> str:
    message = _generate_unencrypted_key(owner, lifetime, level)
    message = password_encrypt(message, key)
    return _sign_key(message)


def write_key(owner: str, lifetime: int, level: int, serial_number: str, disk: str):
    key = generate_key(serial_number)
    message = _generate_crypted_key(owner, lifetime, level, key)
    with open(f'{disk}\\secret.key', 'w') as f:
        f.write(message)


if __name__ == '__main__':
    key = _generate_crypted_key('Kivi', 123, 3, 'secret')
    print(key)
