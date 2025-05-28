print("Intorduzca los extremos de un intervalo cerrado")
inf=int(input("Intervalo inferior: "))
sup=int(input("Intervalo superior: "))

suma=0
contador=0

if(sup>inf):
    n=int(input("Numero para dividir: "))
    print("**************************************")
    print("Los numeros divisibles son:",end=" ")
    for i in range (inf,sup+1):
        if (i%n==0):
            contador=contador+1
            suma=suma+i
            print(i,end=" ")
    print("\nSuma de los",contador,"numeros divisibles =",suma)

else:
    print("Extremo inferior mayor que el extremo superior!!!")
