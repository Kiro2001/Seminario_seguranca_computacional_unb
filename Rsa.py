from geradorchaveRsa import mainCriarChave

def encrip(msg,chav):
    cif=pow(msg,chav[0],chav[1])
    return cif

def decrip(cif,chav):
    msg=pow(cif,chav[0],chav[1])
    return msg

    
chaves=mainCriarChave()
chavpub=chaves[0]
chavpriv=chaves[1]

msg=104

cif=encrip(msg,chavpub)
print(cif)

msg1=decrip(cif,chavpriv)
print(msg1)