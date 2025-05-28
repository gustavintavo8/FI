def digitos(n,base):
    cadena=""
    elem=n
    while(elem>0):
        digito=elem%base
        #if elif para digitos del 10(A) al 15(F)
        cadena=str(digito)+" "+cadena
        elem=elem//base
    return cadena

print(digitos(254,10))
print(digitos(254,2))
print(digitos(254,8))

print(digitos(254,16)) #no funciona(Linea 6)
