#ejercicio 8
#se le solicita al usuario todos los datos requeridos
dato= str(input("¿la edad que desea ingresar en es en meses o en años? ")) #se le dice a la persona si quiere poner la edad en meses o en años
edad=int(input("ingrese su edad:")) #se pide que ingrese la edad 
sexo = str(input("ingrese su genero")) #se le pide el genero de la persona

if dato not in ["meses", "años"]: 
    print(f"el dato que digito es invalido, ingrese 'años' o 'meses'.")  #si el dato que ingreso es invalido le pide otra vez que ingrese lo pedido
    exit #finaliza el programa si es valida
if dato == "años": #convierte la edad a meses si el tipo de dato es 'años'
    Convertirmeses = edad * 12
    Nivelhemoglobina = int(input("¿que nivel de hemoglobina presenta el cliente?"))
    #se solicita la cantidad de hemoglobina por decilitro que tiene el cliente
else:
   #si la edad ya esta en meses, se asigna directamente
    Convertirmeses = edad
    #se solicita el nivel de hemoglobina en gramos por decilitro
    Nivelhemoglobina = int(input("¿que nivel de hemoglobina tiene el paciente?"))
    #determina el rango minimo de hemoglobina basado la edad por meses
if Convertirmeses  >= 0 and Convertirmeses <= 1:
    rangoMin = 13
elif Convertirmeses > 1 and Convertirmeses <= 6:
    rangoMin = 10
elif Convertirmeses > 6 and Convertirmeses <= 12:
    rangoMin = 11
elif Convertirmeses > 12 and Convertirmeses <= 60:
    rangoMin = 11.5
elif Convertirmeses > 60 and Convertirmeses < 120:
    rangoMin = 12.6
elif Convertirmeses >= 120 and Convertirmeses <= 180:
    rangoMin = 13
    
    #si la edad del paciente es mayor de 15 años se ajusta el rango minimo segun el sexo
else:
    if sexo == "mujer" and Convertirmeses > 180:
        rangoMin = 12
    elif sexo == "hombre" and Convertirmeses >180:
        rangoMin =14
        #determina si el paciente tiene hemoglobinacon el rango minimo
if Nivelhemoglobina < rangoMin:
    resultado = "positivo para anemia"
else:
    resultado = "negativo para anemia"
    #imprime el resultado del analisis
print("resultado:", resultado)



