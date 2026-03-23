print('seleciones el tipo de conexion')
print('para conexiones en serie pulse 1')
print('para conexiones en paralelo pulse 2')
conexion= int(input('ingrese la conexion deseada:'))
numresistencias=int(input('ingrese el numero de resistencias:'))
resistenciaeq=0
for i in range(1,numresistencias+1):
    resistencias=float(input(f'ingrese el valor de cada resistencia {i}:'))

if conexion==1:
    resistenciaeq=resistencias+resistencias
elif conexion == 2 :
    resistenciaeq=(1/resistencias)+(1/resistencias)

if conexion == 1:
    print(f"\nLa resistencia equivalente en SERIE es: {resistenciaeq:.2f} Ω")
elif conexion == 2:
    print(f"\nLa resistencia equivalente en PARALELO es: {resistenciaeq:.2f} Ω")