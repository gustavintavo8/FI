r = float(input("Radio de la circunferencia: "))

print("Escoja una opcion:")
print("a/ Calcular la longitud")
print("b/ Calcular el area")
print("a/ Calcular el volumen")
print("q/ SALIR")

opcion=str(input("?: "))

while(opcion!='q' or opcion!='Q'):

    if (opcion=='a' or opcion=='A'):
        longitud = 2 * 3.1416 * r
        print("Longitud con radio",r,"=",longitud)

    elif(opcion=='b' or opcion=='B'):
        area=3.1416*(r**2)
        print("Area con radio",r,"=",area)

    elif(opcion=='c' or opcion=='C'):
        volumen=4/3*3.1416*(r**3)
        print("Volumen con radio",r,"=",volumen)

    print()
    print("Escoja una opcion:")
    print("a/ Calcular la longitud")
    print("b/ Calcular el area")
    print("a/ Calcular el volumen")
    print("q/ SALIR")

    opcion=str(input("?: "))
