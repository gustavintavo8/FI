l2=[3,5,7,9]

#sum(l2)
#len(l2)
suma=0
print(l2,"Longitud: ",len(l2))
for i in range(len(l2)): #range(0,len(l2),1)
    #print(i,l2[i]) #posicion,valor de esa posicion
    suma=suma+l2[i]

print("suma =",suma)

l1=[]
for j in range(1,21):
    if j%2==0:
        l1.append(j) #meter elementos a la lista
print(l1)

#l3=l1+l2 (Para concatenar listas)
#nombre="Manolo"
#len(nombre)=6
#nombre(0)=M
