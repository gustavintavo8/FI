def suma(lista):
    s=0
    for i in range(len(lista)):
        s=s+lista[i]
    return s

def cuenta_as(cadena):
    cont=0
    for i in range(len(cadena)):
        if cadena[i]=='a' or cadena[i]=='A':
            cont=cont+1
    return cont

print("Suma =",suma([1,2,3,4,5]))
c="Manolo"
num_a=cuenta_as(c)
print("As =",num_a)
