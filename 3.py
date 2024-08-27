monto=int(input("digite el monto total de su compra:"))
if monto>500000:
    inver = int(monto * 0.55)
    prestamo = int(monto * 0.30)
    credito = int(monto * 0.15 )
    print(f"el valor invertido{inver}, el valor prestado del banco es{prestamo}, el valor del credito es {credito}")
elif monto<500000:
      inver = int(monto * 0.70)
      restante = int(monto * 0.30)
      intereses = int(restante * 0.2)
      restante = int(restante + intereses)
      print(f"el valor invertido{inver}, el credito  es{restante}, los intereses del credito son{intereses} ")




  
