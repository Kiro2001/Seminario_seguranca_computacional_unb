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

    ps = b"\x00" * (k - tam_mensagem - 2 * h.bit_length() - 2)
    db = h.to_bytes(h.bit_length()) + ps + b"\x01" + mensagem
    seed = os.urandom(h.bit_length())
    db_mask = mgf1(db, k - h.bit_length(), TAMANHO_HASH_H)
    seed_mask = mgf1(db_mask, h.bit_length(), TAMANHO_HASH_H)
    masked_db = xor_bytes(db, db_mask)
    masked_seed = xor_bytes(seed, seed_mask)
    return masked_seed + masked_db


def cifrar(mensagem: Union[int, str], chave: tuple[int, int]) -> int:
    if isinstance(mensagem, str):
        mensagem = int.from_bytes(mensagem.encode("utf-8"))
    _, n = chave
    n_bytes = (n.bit_length() + 7) // 8
    bytes_mensagem = mensagem.to_bytes(n_bytes)
    mensagem_codificada = codificar_oaepp(bytes_mensagem, n_bytes)
    return criptografar(int.from_bytes(mensagem_codificada), chave)
