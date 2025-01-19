import random

#gerador de número aleatorio que depois vai passar pelo teste de primabilidade para decidir se o número é primo
def geradornumale(bits):
    num=random.randrange((2**(bits-1))+1, (2**bits)-1)
    return num


num=geradornumale(1024)
print(num)