import random


# gerador de número aleatorio que depois vai passar pelo teste de primabilidade para decidir se o número é primo
def geradorNumAle(bits: int):
    num = random.randrange((2 ** (bits - 1)) + 1, (2**bits) - 1)
    return num


def eprimo_Miller_Rabin(num):
    if num <= 1:
        return False
    if (num == 2) or (num == 3):
        return True
    elif num % 2 == 0:
        return False
    else:
        num1 = num - 1
        exp = 1
        while num1 % (2**exp) == 0:
            exp += 1
        exp -= 1
        mul = num1 // (2**exp)
        num2 = random.randrange(2, num1)
        num3 = pow(num2, mul, num)
        if (num3 == 1) or (num3 == num1):
            return True
        else:
            while mul != num1:
                num3 = pow(num3, 2, num)
                mul *= 2
                if num3 == num1:
                    return True
                elif num3 == 1:
                    return False


def geradorPrimo(n_bits: int):
    while True:
        num = geradorNumAle(n_bits)
        if num % 2 != 0:
            if eprimo_Miller_Rabin(num):
                return num


def mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a


def algEucExt(a: int, b: int) -> tuple:
    if a == 0:
        return b, 0, 1
    else:
        mdc, x1, y1 = algEucExt(b % a, a)
        x = y1 - (b // a) * x1
        y = x1

    return [mdc, x, y]


def criarChavePublica(phi):
    while True:
        num = geradorNumAle(100)
        if (num % 2) != 0:
            if mdc(phi, num) == 1:
                break
    return num


def criarChavePrivada(p: int, q: int, e: int, phn: int) -> int:
    res = algEucExt(phn, e)
    pd = res[2]
    if pd > 0:
        d = pd
    else:
        d = phn + pd
    return d


def criarChaves(n_bits: int) -> list:
    p = geradorPrimo(n_bits)
    q = geradorPrimo(n_bits)
    while q == p:
        q = geradorPrimo(n_bits)
    n = p * q
    phn = (p - 1) * (q - 1)
    e = criarChavePublica(phn)
    chave_publica = [e, n]
    chave_privada = [pow(e, -1, phn), n]
    return [chave_publica, chave_privada]
