import math
import hashlib
import os
from rsa import criptografar, descriptografar


def mgf1(seed: bytes, k: int, tam_hash: int = 20) -> bytes:
    t = b""
    for i in range(math.ceil(k / tam_hash)):
        c = seed + i.to_bytes(4)
        t += hashlib.sha1(c).digest()
    return t[:k]


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def codificar_oaep(mensagem_em_bytes: bytes, k: int, rotulo: bytes = b""):
    db = (
        hashlib.sha1(rotulo).digest()
        + b"\x00"
        * (k - len(mensagem_em_bytes) - 2 * len(hashlib.sha1(rotulo).digest()) - 2)
        + b"\x01"
        + mensagem_em_bytes
    )
    seed = os.urandom(len(hashlib.sha1(rotulo).digest()))
    db_mask = mgf1(seed, k - len(hashlib.sha1(rotulo).digest()) - 1)
    masked_db = xor_bytes(db, db_mask)
    seed_mask = mgf1(masked_db, len(hashlib.sha1(rotulo).digest()))
    masked_seed = xor_bytes(seed, seed_mask)
    return b"\x00" + masked_seed + masked_db


def decodificar_oaep(texto_cifrado: bytes, k: int, rotulo: bytes = b""):
    masked_seed, masked_db = (
        texto_cifrado[1 : 1 + len(hashlib.sha1(rotulo).digest())],
        texto_cifrado[1 + len(hashlib.sha1(rotulo).digest()) :],
    )
    seed_mask = mgf1(masked_db, len(hashlib.sha1(rotulo).digest()))
    seed = xor_bytes(masked_seed, seed_mask)
    db_mask = mgf1(seed, k - len(hashlib.sha1(rotulo).digest()) - 1)
    db = xor_bytes(masked_db, db_mask)
    for i in range(len(hashlib.sha1(rotulo).digest()), len(db)):
        if db[i] == 0:
            continue
        elif db[i] == 1:
            break

    return db[i + 1 :]


def cifrar(mensagem_em_bytes: bytes, chave_publica: tuple[int, int]):
    _, n = chave_publica
    k = (n.bit_length() + 7) // 8
    mensagem_codificada = codificar_oaep(mensagem_em_bytes, k)
    mensagem_cifrada = criptografar(int.from_bytes(mensagem_codificada), chave_publica)
    return mensagem_cifrada.to_bytes(k)


def decifrar(texto_cifrado: bytes, chave_privada: tuple[int, int]):
    _, n = chave_privada
    k = (n.bit_length() + 7) // 8
    mensagem_decodificada = descriptografar(
        int.from_bytes(texto_cifrado), chave_privada
    )
    return decodificar_oaep(mensagem_decodificada.to_bytes(k), k)
