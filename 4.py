#ejercicio 4
import random
colores = ['verde','rojo','azul','amarillo','negro','blanco']
valor =int(input("ingrese su valor"))

pcchoice = random.choice (colores)

print(f'la balota sacada es: {pcchoice}')

if pcchoice == 'rojo':
    descuento= valor * 0.15
    valorFinal = valor - descuento
    print(f"el valo del producto es {valor}, el color que es {pcchoice},el valor con el descuentoes {descuento}")
elif pcchoice == 'verde':
    descuento = valor * 0.20
    valor_fi = valor - descuento
    print(f"el valor del producto es {valor}, el color que saco es {pcchoice}, el valor con el descuento es {valor_fi}")
else :
    print(f"el color es {pcchoice} por lo tanto no hay descuento")