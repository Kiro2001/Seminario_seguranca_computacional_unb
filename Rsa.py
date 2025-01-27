import hashlib
import base64
from geradorchaveRsa import criarChaves
from obase64 import codificarb64


def criptografar(mensagem: int, chave: int) -> int:
    cif = pow(mensagem, chave[0], chave[1])
    return cif


def descriptografar(mensagem_cifrada: int, chave: int):
    msg = pow(mensagem_cifrada, chave[0], chave[1])
    return msg


def assinar(mensagem: str, chave: int):
    hash = hashlib.sha3_256(mensagem.encode("utf-8")).hexdigest()
    assinatura = criptografar(int(hash, 16), chave)
    n_bytes = (assinatura.bit_length() + 7) // 8
    bytes_assinatura = assinatura.to_bytes(n_bytes, byteorder="big")
    return base64.b64encode(bytes_assinatura).decode("ascii")


chave_publica, chave_privada = criarChaves(1024)

msg = "mensagem qualquer"
assinatura = assinar(msg, chave_privada)
print(assinatura)
