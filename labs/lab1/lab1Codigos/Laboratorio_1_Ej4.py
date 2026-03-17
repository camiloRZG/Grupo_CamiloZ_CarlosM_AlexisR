##implemento el while true que significa mientras sea verdad
while True: 
        #primero realizo el input para que el usuario ingrese los grados en Celsius
        grados = float(input("Ingresar grados Celsius: "))

        #creo una condición por si el valor ingresado es menor a 20 sea invalido ya que no se especifica
        if grados < 20:
            print("valor invalido")
            print("--------------------------------------------------")
        #creo otra condicion si grados esta entre los dos valores solicitados va a mostrar un "estado normal"
        elif 20 <= grados <= 45:
            print("estado normal")
            print("--------------------------------------------------")
        #condicion para los rangos entre 45 y 75 grados muestra "advertencia, encendiendo ventiladores auxiliares"
        elif 45 < grados <= 75:
            print("advertencia, encendiendo ventiladores auxiliares")
            print("--------------------------------------------------")
        #condicion para cuando los grados son mayores de 75 muestra "¡PeligroCrítico!Apagando servidor de emergencia", a su vez como se solicito
        #se crea un break para finalizar el while true sino la maquina seguiria pidiendo un input
        elif grados > 75:
            print("¡PeligroCrítico!Apagando servidor de emergencia")
            print("--------------------------------------------------")
            break 