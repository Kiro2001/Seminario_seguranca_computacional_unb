import hashlib


def hash_g(bytes_: bytes) -> int:
    hash = hashlib.sha256(bytes_).hexdigest()
    return int(hash, 16)


def hash_h(bytes_: bytes) -> int:
    hash = hashlib.sha1(bytes_).hexdigest()
    return int(hash, 16)
