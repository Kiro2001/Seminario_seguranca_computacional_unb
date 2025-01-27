lstchr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def codificarb64(string):
    strascii = string.encode("ascii")
    strb64 = ""

    for i in range(0, len(strascii), 3):
        val = 0
        cont = 0
        for j in range(i, min(i + 3, len(strascii))):
            val = val << 8
            val = val | strascii[j]
            cont += 1
        numbits = cont * 8
        padding = numbits % 3
        val = bin(val)
        val = val[2::]
        val = "0" + val

        if padding != 0:
            val += ((8 * padding) - 6) * "0"

        for k in range(4 - padding):
            ind = k * 6
            val2 = val[ind : ind + 6]
            print(val2)
            strb64 += lstchr[int(val2, 2)]

        for i in range(padding):
            strb64 += "="

    return strb64
