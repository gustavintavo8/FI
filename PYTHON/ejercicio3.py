m=int(input("Introduzca filas: "))
n=int(input("Introduzca columnas: "))

for i in range (1,m+1): #itero por las filas
    #print("A",i,sep="",end="") #numero de fila
    for j in range (1,n+1): #itero por las columnas
        print("A",i,j,sep="",end=" ") #numero de columna
    print()
