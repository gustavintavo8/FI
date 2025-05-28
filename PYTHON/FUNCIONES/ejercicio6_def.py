def IMC(peso,altura):

    if peso<=0 or altura<=0:
        return ("Datos incorrectos")

    imc=peso/altura**2

    if(imc<18.5):
        return("Bajo peso")
    elif(18.5>=imc<25):
        return("Normal")
    elif(25>=imc<30):
        return("Sobrepeso")
    return("Obesidad")

peso=float(input("Introduce tu peso: "))
altura=float(input("Introduce tu altura: "))

print(IMC(peso,altura))
