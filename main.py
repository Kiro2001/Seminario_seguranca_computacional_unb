from geradorchaveRsa import criarChaves
from Rsa import assinar
import oaep

chave_publica, chave_privada = criarChaves(1024)

msg = "mensagem qualquer"
assinatura = assinar(msg, chave_privada)
print(assinatura)


print(oaep.cifrar(msg, chave_publica))
