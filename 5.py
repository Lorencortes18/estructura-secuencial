nombre=str(input("escribe tu nombre"))
sexo= str(input("¿cual es su sexo?"))
edad= int(input("¿cual es su edad?"))

if sexo=="femenino":
   print(f"Señor {nombre} el numero de pulsaciones que usted deberia tener por cada 10 seg de ejercicio aerobico es {(220-edad)/10}")
elif sexo=="masculino":
    print(f"Señor {nombre} el numero de pulsaciones que usted deberia tener por cada 10 seg de ejercicio aerobico es {(210-edad)/10}")
    
else:
    print(f"informacion incorrecta")




