zap=int(input("¿cuantas zapatillas vas a comprar? "))
valorzap= zap*100000
if zap>=3:
    descuento= int(valorzap * 0.2)
    valorfinal= int (valorzap - descuento)
    print(f"El valor de tu compra es {valorzap}, el valor del descuento {descuento}, el valor a pagar es {valorfinal}")
else:
    descuento= valorzap * 0.1
    valorfinal= int(valorzap - descuento)   
    print(f" el valor de tu compra es { valorzap}, el valor del descuento es {descuento}, el valor a pagar es {valorfinal}")