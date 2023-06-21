from secrets import token_hex

import pytest
from cryptography.fernet import Fernet

from decorators_cryptography import decrypt, encrypt

key = Fernet.generate_key()


@encrypt(key)
def encrypt_data(data):
    return data


@decrypt(key)
def decrypt_data(data):
    return data


def test_encrypt():
    test_word = token_hex(20)

    assert test_word == decrypt_data(encrypt_data(test_word))
