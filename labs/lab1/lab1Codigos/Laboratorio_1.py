##Laboratorio 1

## Ejercicio 1 Ley de Ohm y Alerta de Potencia
#ingresar el valor de voltaje y corriente en este caso usare enteros
voltaje = int(input("ingresar voltaje = "))
corriente = int(input("ingresar corriente = "))

#Defino y calculo las variables 
resistencia = voltaje/corriente
potencia = voltaje*corriente

#Print de variables
print("resistencia:",resistencia)
print("potencia:",potencia)

#Condicionamiento con un comando if si es mayor a 100 print el mensaje y si es menor o igual a 1000 el otro print
if potencia>1000:
    print("¡Peligro!, Alta disipación de potencia detectada.")
    print("--------------------------------------------------")
elif potencia <= 1000:
    print("Operacion en rangos seguros")
    print("--------------------------------------------------")

##Ejercicio 2
#Ingresar valor de voltaje y voltaje minimo de operacion como pide horas enteras usare int para todo
voltaje = int(input("ingresar voltaje = "))
voltaje_min = int(input("ingresar voltaje minimo de operacion = "))

#inicio un contador para las horas
n = 0
#un ciclo while mientras el voltaje sea mayor al operacional siga ejecutando
while voltaje>=voltaje_min:
        n += 1
        voltaje = voltaje*0.97

print("horas enteras:", n)
print("--------------------------------------------------")

##Ejercicio 3
#inicio la variable para poder condicionar el while


while True:
#muestro primero las opciones y luego hago el input para seleccionar la opcion
#realizo print de cada una de las opciones disponibles
    print("1. Convertir miliamperios (mA) a amperios (A).")
    print("2. Convertir microfaradios (µF) a faradios (F).")
    print("3. Convertir kiloohmios (kΩ) a ohmios (Ω).")
    print("4. Salir.")

#solicito al usuario seleccionar la variable
    variable = int(input("Seleccionar Opción = "))

#inicio los condicionales para cada variable que sea seleccionada y una opcion final por si la opcion seleccionada no es valida, en este caso usare floating porque los valores
#ingresados pueden ser decimales 
#si la variable seleccionada es el 1 calcular los ma
    if variable == 1:
        miliamperios = float(input("Ingresar Miliamperios = "))
        print(f"amperios = {miliamperios/1000}")
        print("--------------------------------------------------")
#si la variable seleccionada es 2 calcular mf
    elif variable == 2:
        microfaradios = float(input("Ingresar Microfaradios = "))
        print(f"faradios = {microfaradios/1000000}")
        print("--------------------------------------------------")
#si la variable seleccionada es 3 calcular ko
    elif variable ==3:
        kiloohmios =  float(input("Ingresar Kiloohmios = "))
        print(f"ohmios = {kiloohmios*1000}")
        print("--------------------------------------------------")
#si la variable seleccionada es 4 salir del programa
    elif variable == 4:
        print("Se finalizó el programa")
        print("--------------------------------------------------")
        break
#si la variable es cualquier otro numero saldremos con un invalido
    else: print("Seleccion invalida")

         







