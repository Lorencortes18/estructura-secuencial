alumno= str(input("¿cual es su nombre?:"))
UltimoPromedio = int(input("¿cual es tu promedio?"))
pension= int(input("¿cuanto paga por pension?:"))

if UltimoPromedio >= 4.0:
   descuento = 0.30 * pension
else:
   descuento = 0.0


ValorDescuento= pension - descuento
ValorFinal= ValorDescuento + (0.10 * ValorDescuento)

print(f"valor de la pension original: {pension}")
print(f"descuento aplicado: {descuento}")
print(f"valor a pagar con iva incluido: {ValorFinal}")