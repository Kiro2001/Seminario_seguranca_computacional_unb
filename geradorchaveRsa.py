import random

#gerador de número aleatorio que depois vai passar pelo teste de primabilidade para decidir se o número é primo
def geradorNumAle(bits):
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
                    return True
                elif num3 == 1:
                    return False


def geradorPrimo():
    while True:
        num=geradorNumAle(1024)
        if num % 2 != 0:
            if eprimo_Miller_Rabin(num):
                return num

def algEucExt(a,b):
    if a==0:
        return b,0,1
    else:
        mdc,x1,y1=algEucExt(b%a,a)
        x=y1 - (b//a) *x1
        y=x1

    return [mdc,x,y]

def criarChavepriv(p,q,e):
    phn=(p-1)*(q-1)
    res=algEucExt(phn,e)
    pd=res[2]
    if pd > 0 :
        d=pd
    else:
        d=phn + pd
    return d

def mainCriarChave(p,q):
    p=geradorPrimo()
    q=geradorPrimo()
    while q == p:
        q=geradorPrimo()
    n=p*q
    e = 65537
    chavpub=[n,e]
    chavpriv=criarChavepriv(p,q,e)
    return [chavpub,chavpriv]





