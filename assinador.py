import base64

import oaep
from rsa import gerarAssinatura

def assinar_msg(msg,chave_pri):
    assinatura = gerarAssinatura(msg, chave_pri)
    return assinatura.decode("utf-8")
def assinar_documento(
    mensagem_claro: str,
    chave_publica: tuple[int, int],
    chave_privada: tuple[int, int],
    nome_arquivo: str = "mensagem.txt",
):
    assinatura = gerarAssinatura(mensagem_claro, chave_privada)
    mensagem_cifrada = oaep.cifrar(mensagem_claro.encode("utf-8"), chave_publica)

    with open(nome_arquivo, "w") as f:
        f.write(base64.b64encode(mensagem_cifrada).decode("utf-8"))
        f.write("\n")
        f.write(assinatura.decode("utf-8"))
