def digitos(n):
    cadena=""
    elem=n
    while(elem>0):
        digito=elem%10
        cadena=str(digito)+cadena
        elem=elem//10
    return cadena

#Ej: digitos(256) retornaria la cadena "256"
#no vale usar str(num)

print(digitos(256))

