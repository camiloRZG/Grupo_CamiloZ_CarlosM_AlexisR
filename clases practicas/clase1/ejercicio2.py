n=int(input('ingrese el valor deseado:'))

if n ==0:
    print('El valor del factorial 0 es igual a 1')
elif n < 0: 
    print('ingrese un numero positivo')
else:
 factorial=1
 for i in range(1,n+1):
  factorial= factorial*i
  print(f'factorial de {i} es {factorial}')
   

   
 

 
 






