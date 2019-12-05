import re

text = ("There were a king with a large jaw and a queen with a plain face, on the throne of England; there were a king with a large jaw and a queen witha fair face, on the throne of France. In both countries it was clearerthan crystal to the lords of the State preserves of loaves and fishes, that things in general were settled for ever.")
palabras = text.split()
lista = []
unicas = []

def listatexto(texto):
    for x in palabras:
        lista.append(x)
        for y in lista:
            if y not in unicas:
                unicas.append(y)
    for z in unicas:
        z = re.sub('[,.:;!"¡?]', '',z)
        print(z)

listatexto(text)

## Practica 4 ##

print("Practica ordenar lista.")

def ordenar(text):
    unicas.sort(key = len)
    print(unicas)

ordenar(text)



