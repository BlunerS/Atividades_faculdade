nuvens = [0,0,0,0,0,1,0]

def pular_nuvens(nuvens):
    saltos = 0
    indice = 0
    while indice < (len(nuvens) - 2):
        if nuvens[indice + 2] != 1:
            saltos += 1
            indice += 2
        else:
            saltos += 1
            indice += 1
    return saltos

print(pular_nuvens(nuvens))