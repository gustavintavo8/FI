umbral=int(input("Introduzca un umbral: "))

for a in range(1,umbral+1):
    #a=int(input("Introduzca un numero: "))
    elemento=a
    suma=0

    while (elemento!=0):
        dig=elemento%10
        suma=suma+(dig**3)
        elemento=elemento//10

    if (a==suma):
        print("La suma es",suma)
