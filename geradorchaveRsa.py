import random

#gerador de número aleatorio que depois vai passar pelo teste de primabilidade para decidir se o número é primo
def geradornumale(bits):
    num=random.randrange((2**(bits-1))+1, (2**bits)-1)
    return num

def eprimo_Miller_Rabin(num):
    res=False
    if (num == 1) or (num == 2) or (num == 3):
        return True
    elif num % 2 == 0:
        return False
    else:
        num1=num - 1
        exp=1
        while(num1%(2**exp) == 0):
            exp+=1
        exp-=1
        mul=num1 // (2**exp)
        num2=random.randrange(2,num1)
        num3=pow(num2,mul,num)
        if (num3 == 1) or (num3 == num1):
            res=True
        else:
            while mul != num1:
                num3=pow(num3,2,num)
                mul*=2
                if num3 == num1:
                    res=True
                    break
                elif num3 == 1:
                    break



    
    return res
def geradorprimo():
    while True:
        num=geradornumale(1024)
        if num % 2 != 0:
            if eprimo_Miller_Rabin(num):
                return num

p=geradorprimo()
q=geradorprimo()

while q == p:
    q=geradorprimo()
print(p)
print(q)
