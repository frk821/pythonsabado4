#Construir un programa que reciba números enteros y los sume mientras estos sean positivos,
#si se digita un numero negativo el programa debe terminar

numero=int(input("Ingresa un numero: "))
while(numero>0):
    
    if(numero>0):
        numero=+numero
    print(numero)    
else:
    print("Ingresaste un numero negativo")