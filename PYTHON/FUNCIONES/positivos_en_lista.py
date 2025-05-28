def lista_pos():
    lista=[]
    n=int(input("Introduce un positivo: "))

    while(n>=0):
        lista.append(n)
        n=int(input("Introduce un positivo: "))
    return lista

print(lista_pos())
