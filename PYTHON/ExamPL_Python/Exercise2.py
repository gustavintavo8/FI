n=int(input('Give a number grater than 0: '))
suma=1
fact=1
for i in range (1,n+1):
    fact=fact*i
    suma=suma+1/fact
print(suma)
