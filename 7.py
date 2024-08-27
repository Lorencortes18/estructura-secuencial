#ejercicio n.7
Cantidadllantas= int(input("ingrese la cantidad de llantas: "))
if Cantidadllantas < 0:
    print(f" numero ingresado incorrecto ")
elif Cantidadllantas < 5:
    precio = 300000
    total = precio * Cantidadllantas
elif Cantidadllantas >= 5 and Cantidadllantas <=10:
    precio= 250000
    total = precio * Cantidadllantas
else:
    precio = 200000
    total = precio * Cantidadllantas
print(f"la cantidad total a pagar es ${precio}, siendo un total de ${total} ")