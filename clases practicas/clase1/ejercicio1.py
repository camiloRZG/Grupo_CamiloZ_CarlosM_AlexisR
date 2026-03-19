numero = int(input("Ingrese un numero: "))
if numero <= 0:
    print('ingrese un numero mayor que 0')
else :
 a=0
 b=1
 contador=0
 print('serie de hasta',numero,'terminos')
 while contador<numero:
    print (f'valor de la serie {a}\n')
    x=a+b
    a=b
    b=x
    contador=contador + 1

