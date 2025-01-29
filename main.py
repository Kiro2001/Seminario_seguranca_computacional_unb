from geradorchaveRsa import criarChaves
from Rsa import assinar
import oaep

chave_publica, chave_privada = criarChaves(1024)

msg = "mensagem qualquer"
assinatura = assinar(msg, chave_privada)
print(assinatura)

mensagem_cifrada = oaep.cifrar(msg, chave_publica)
print(mensagem_cifrada)
mensagem_claro = oaep.decifrar(mensagem_cifrada, chave_privada)
print(mensagem_claro)
