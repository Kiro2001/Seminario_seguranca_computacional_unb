import random

N_ROUNDS_MILLER_RABIN = 4


# gerador de número aleatorio que depois vai passar pelo teste de primabilidade para decidir se o número é primo
def geradorNumAle(bits: int):
    num = random.randrange((2 ** (bits - 1)) + 1, (2**bits) - 1)
    return num


def testeMillerRabin(d: int, n: int):
    a = 2 + random.randint(1, n - 4)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def ehPrimo(n: int):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(N_ROUNDS_MILLER_RABIN):
        if not testeMillerRabin(d, n):
            return False

    return True


def geradorPrimo(n_bits: int):
    while True:
        num = geradorNumAle(n_bits)
        if num % 2 != 0:
            if ehPrimo(num):
                return num


def algEucExt(a: int, b: int) -> tuple:
    if a == 0:
        return b, 0, 1
    else:
        mdc, x1, y1 = algEucExt(b % a, a)
        x = y1 - (b // a) * x1
        y = x1

    return [mdc, x, y]


def criarChavePrivada(p: int, q: int, e: int) -> int:
    phn = (p - 1) * (q - 1)
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
    e = 65537
    chave_publica = [e, n]
    chave_privada = [criarChavePrivada(p, q, e), n]
    return [chave_publica, chave_privada]
