import numpy as np #cargamos libreria 
def comparar_rendimiento(datos: list): #Creamos funcion para que el main pueda llamarla 
    historial_datos=np.array(datos) #convertimos los datos en un arreglo array 
    datos_filtrados=np.unique(historial_datos[:,1]) #extraemos la informacion que nos interesa de los datos. ademas usamos la funcion unique para filtrar datos repetidos 
    cajita_de_datos={}# creamos un diccionario vacio para posteriormente guardarlos aqui
    for modelo in datos_filtrados: #comenzamos ciclo for para recorrer dato por dato
         datrobot=historial_datos[historial_datos[:, 1] == modelo] #aplicamos masacar booleana para filtrar los datos y solo dejar los que nos importan 
         bateria = datrobot[:, 4].astype(float)#extraemos toda la columna 4 de las baterias 
         basura_total = datrobot[:, 5].astype(float)#extraemos toda la columna 5 de las basuritas
         consumo_bateria = 100.0 - bateria[-1]# Calculamos el consumo de bateria, notar que [-1] nos trae el ultimo dato que esta en el vector 
         basura_total = basura_total[-1]#misma logica del [-1] pero aca es para que los datos de basura y bateria sean consistentes al momento de calcular la eficiencia 
         if consumo_bateria == 0:#condicional para evitar diviciones indeseadas 
              eficiencia=(0.0)
         else:
              eficiencia= basura_total/consumo_bateria#calculo de la eficiencia 
         cajita_de_datos[modelo]={  #metemos todo los datos ya filtrados en nuestra cajita de datos 
         'consumo_bateria':consumo_bateria,
         'basura_total':basura_total,
         'eficiencia':eficiencia     
        }
    return cajita_de_datos      #retormanos los datos ya filtradados 
               

        

