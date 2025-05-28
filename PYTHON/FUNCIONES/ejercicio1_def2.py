def factorial(n):
    #if es_par(n):
    #   return -1
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac

def es_par(num): #se pueden integrar varias funciones
    if num%2==0:
        return True
    return False

#programa principal
num=int(input("Introduce un numero: "))
while(num<0):
    num=int(input("Introduce un numero: "))

print(factorial(num))
