#
observador=10

print("**MENU**")
print("0.SALIR")
print("1.Saludar")
print("2.Despedir")
while(observador != 0):
    observador=int(input("Digite una opción: "))
    if(observador==0):
        break
    elif(observador==1):
        print("qhubo mijo")
    elif(observador==2):
        print("suerte mijo")
    else:
        print("Digite una opción válida")
else:
    print("Terminé")