from geradorchaveRsa import criarChaves
from Rsa import assinar,verificarAssinatura
import oaep

chave_publica, chave_privada = criarChaves(1024)

msg = "mensagem qualquer"
assinatura = assinar(msg, chave_privada)
print(assinatura.decode("utf-8"))
print("")

mensagem_cifrada = oaep.cifrar(msg.encode("utf-8"), chave_publica)
print(mensagem_cifrada)
print("")
mensagem_claro = oaep.decifrar(mensagem_cifrada, chave_privada)
mensagem_claro=mensagem_claro.decode("utf-8")
print(mensagem_claro)

mensagem_claro1=mensagem_claro + " "


print(verificarAssinatura(mensagem_claro,chave_publica,assinatura))
print(verificarAssinatura(mensagem_claro1,chave_publica,assinatura))

mensagem_claro1=mensagem_claro1[0:-1]

print(verificarAssinatura(mensagem_claro,chave_publica,assinatura))