import base64

from rsa import verificarAssinatura
import oaep


def verificar_documento(
    nome_arquivo: str, chave_publica: tuple[int, int], chave_privada: tuple[int, int]
) -> bool:
    with open(nome_arquivo, "r") as f:
        mensagem_cifrada = base64.b64decode(f.readline())
        assinatura = f.readline().encode("utf-8")
    mensagem_claro = oaep.decifrar(mensagem_cifrada, chave_privada).decode("utf-8")
    print(f"Mensagem decifrada: {mensagem_claro}")
    return verificarAssinatura(mensagem_claro, chave_publica, assinatura)
