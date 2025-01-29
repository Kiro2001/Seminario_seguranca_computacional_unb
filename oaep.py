import hashlib
import os
import math
from typing import Union

from Rsa import criptografar, descriptografar


TAMANHO_HASH_H = 20


def mgf1(seed: bytes, k: int, tam_hash: int) -> bytes:
    t = b""
    for i in range(math.ceil(k / tam_hash)):
        c = seed + i.to_bytes(4)
        t += hashlib.sha1(c).digest()
    return t[:k]


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def codificar_oaepp(mensagem: bytes, k: int, rotulo: bytes = b"") -> bytes:
    h = int(hashlib.sha1(rotulo).hexdigest(), 16)
    tam_mensagem = len(mensagem)

    ps = b"\x00" * (k - tam_mensagem - 2 * ((h.bit_length() + 7) // 8) - 2)
    db = h.to_bytes(((h.bit_length() + 7) // 8)) + ps + b"\x01" + mensagem
    seed = os.urandom(((h.bit_length() + 7) // 8))
    db_mask = mgf1(db, k - ((h.bit_length() + 7) // 8), TAMANHO_HASH_H)
    seed_mask = mgf1(db_mask, ((h.bit_length() + 7) // 8), TAMANHO_HASH_H)
    masked_db = xor_bytes(db, db_mask)
    masked_seed = xor_bytes(seed, seed_mask)
    return masked_seed + masked_db


def decodificar_oaep(mensagem: bytes, k: int, rotulo: bytes = b"") -> bytes:
    h = int(hashlib.sha1(rotulo).hexdigest(), 16)
    masked_seed = mensagem[: ((h.bit_length() + 7) // 8)]
    masked_db = mensagem[((h.bit_length() + 7) // 8) :]
    seed_mask = mgf1(masked_db, ((h.bit_length() + 7) // 8), TAMANHO_HASH_H)
    seed = xor_bytes(masked_seed, seed_mask)
    db_mask = mgf1(seed, k - ((h.bit_length() + 7) // 8), TAMANHO_HASH_H)
    db = xor_bytes(masked_db, db_mask)
    i = (h.bit_length() + 7) // 8
    while db[i] == 0:
        i += 1
    return db[i + 1 :]


def cifrar(mensagem: Union[int, str], chave: tuple[int, int]) -> int:
    if isinstance(mensagem, str):
        print(mensagem.encode("utf-8"))
        mensagem = int.from_bytes(mensagem.encode("utf-8"))
    _, n = chave
    n_bytes = (n.bit_length() + 7) // 8
    bytes_mensagem = mensagem.to_bytes(n_bytes)
    mensagem_codificada = codificar_oaepp(bytes_mensagem, n_bytes)
    return criptografar(int.from_bytes(mensagem_codificada), chave)


def decifrar(mensagem: int, chave: tuple[int, int]) -> str:
    _, n = chave
    n_bytes = (n.bit_length() + 7) // 8
    mensagem_decifrada = descriptografar(mensagem, chave)
    bytes_mensagem = decodificar_oaep(mensagem_decifrada.to_bytes(n_bytes), n_bytes)
    return bytes_mensagem.decode("utf-8")
