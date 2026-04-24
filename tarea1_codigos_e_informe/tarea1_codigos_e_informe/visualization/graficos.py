import matplotlib.pyplot as plt
import os
#Parte A

def plot_metricas(diccionario_experimentos,ambiente,ruta):                      #Primero defino la funcion con las variables de entrada en este caso los datos del diccionario,
                                                                                #el ambiente que quiero y la ruta que quiero
    datos_filtrados = []                                                        #inicializo los listados donde almacenare los valores que necesito
    PPO_Mask = []
    PPO = []

    for clave, valor in diccionario_experimentos.items():                       #inicio un for para recorrer la clave y valor del diccionario.items
        if valor["ambiente"] == ambiente and valor["ruta"] == ruta:             #creo la condicion si en valor ambiente es equivalente al ambiente que necesito y la ruta tambien
                                                                                #entonces se va a agregar a la lista de datos filtrados
            datos_filtrados.append(valor)
    #print(datos_filtrados)


    for i in datos_filtrados:                                                   #Inicio un for en los datos filtrados para separar los datos de PPO Y PPO-Mask
        if i["politica"] == "PPO":                                              #Utilizo la misma logica, si en datos filtrados politica es equivalente a PPO guardar en PPO                                                                
           PPO.append(i) 
        elif i["politica"] == "PPO-Mask":                                       #Luego si politica es equivalente a PPO-Mask guardar en PPO_Mask
           PPO_Mask.append(i)

    print("PPO VALORES:")                                                       #Para verificar que los datos sean los correctos genere estos print para luego hacer una comparacion con los valores independientes
    print(PPO)                                                                  #de ISE, IAE, ITSE, ITAE segun sea el caso de PPO o PPO-Mask
    print("---------------------------------------------------------------")    #Los --- son para separar y dejar mas ordenados los datos 
    print("PPO-Mask VALORES:")
    print(PPO_Mask)
    print("---------------------------------------------------------------")


    def ciclo(datos):                                                           #Cree otra funcion para no tener que ir uno por uno sacando los valores de ISE, IAE, ... 

            ISE = []                                                            #Inicializo las variables
            IAE = []
            ITSE = []
            ITAE = []

            for i in datos:                                                     #Creo un ciclo for que recorra los datos que se ingresan a la funcion en este caso PPO o PPO_Mask
                ISE = i["ISE"]                                                  #Al recorrer el diccionario, cuando se encuentre con la clave ISE le asignare su valor a la variable ISE
                IAE = i["IAE"]                                                  #Lo mismo para las IAE, ITSE, ITAE
                ITSE = i["ITSE"]
                ITAE = i["ITAE"]

            return (ISE,IAE,ITSE,ITAE)                                          #La salida van a ser las 4 variables con sus valores ya guardados
        
    PPO_ISE,PPO_IAE,PPO_ITSE,PPO_ITAE = ciclo(PPO)                              #Doy uso a la funcion para sacar en PPO los valores mencionados de ISE, IAE,...
    PPO_M_ISE,PPO_M_IAE,PPO_M_ITSE,PPO_M_ITAE = ciclo(PPO_Mask)

    plt.figure(figsize=(12,5))                                                  #Creo una figura para plotear las gracias de barras solicitadas                 
                                                                                
    plt.subplot(1,4,1)
    plt.bar(["PPO","PPO-Mask"],[PPO_ISE,PPO_M_ISE], color=['blue','red'])       #Creo el primer grafico de barras con los colores solicitados con "color=" y sus variables respectivas para este caso PPO_ISE Y PPO_M_ISE
    plt.ylabel('Valor del Indice')                                              #Genero el texto para el label Y solicitada
    plt.title('ISE')                                                            #Titulo del grafico de barras 

    plt.subplot(1,4,2)
    plt.bar(["PPO","PPO-Mask"],[PPO_IAE,PPO_M_IAE], color=['blue','red'])       #Esto se repite para los siguientes 3 graficos de barras con sus variables correspondientes 
    plt.title('IAE')

    plt.subplot(1,4,3)
    plt.bar(["PPO","PPO-Mask"],[PPO_ITSE,PPO_M_ITSE], color=['blue','red'])
    plt.title('ITSE')

    plt.subplot(1,4,4)
    plt.bar(["PPO","PPO-Mask"],[PPO_ITAE,PPO_M_ITAE], color=['blue','red'])
    plt.title('ITAE')

    plt.suptitle('Indices de error - real | simple (Tabla 6)' )                 #Genero el titulo de la figura con suptitle
    plt.tight_layout()                                                          #Para que no se superpongan los graficos 
    

    os.makedirs("resultados_graficos", exist_ok=True)                           #Verifico que la carpeta resultados_graficos esté creada, si no lo esta lo va a crear
    direccion = os.path.join("resultados_graficos",                             #Armo la direccion para guardar la figura con el nombre del archivo segun el ambiente y ruta seleccionados desde el main
                f"indices_error_{ambiente}_{ruta}.png")                         

    plt.savefig(direccion, dpi=300)                                             #Guardo la figura en la direccion creada con un dpi de 300 para tener resolucion alta
    plt.show()
    return 

#Parte B

def plot_lidar(angulos,distancias,distancias_norm):

    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plt.scatter(angulos,distancias,c=distancias, cmap='winter')                 #con c=distancias defino que los colores cambien segun los valores de distancias y cmap=winter es el mapa de colores que va a utilizar "
    
    plt.xlabel("Ángulo de giro (0-360°)")
    plt.ylabel("Distancia detectada (m)")
    plt.title("¿A que distancia están los objetos?\n (Eje X: Ángulo | Eje Y: Metros)")
    plt.grid()                                                                  #genero una grilla para mejorar el grafico

    plt.subplot(1,2,2)
    plt.plot(angulos,distancias_norm, marker='o', color='red')
    plt.xlabel("Sectores del Sensor")
    plt.ylabel("Valor 0.0 a 1.1")                                               
    plt.title("Datos Normalizados \n (Lo que procesa la IA)")                   #con \n realizo un salto
    plt.grid()
    plt.tight_layout()


    os.makedirs("resultados_graficos", exist_ok=True)                           #Verifica que la carpeta resultado_graficos esté creada, si no lo está la crea                                                                       
    direccion = os.path.join("resultados_graficos","mapa_lidar.png")            #Armo la direccion para guardar la figura 
    plt.savefig(direccion, dpi=300)                                             #Guardo la figura en la direccion creada con un dpi de 300 para tener resolucion alta

    plt.show()
    
    return

#Parte C

def plot_trayectorias(x_ppo,y_ppo,x_mask,y_mask,waypoints,nombre):

    x_wp = []                                                                   #Inicio los listados vacios
    y_wp = []                                                                   

    for i in waypoints:
        x_wp.append(i[0])                                                       #voy agregando los valores de la primera posicion en x_wp y los de la segunda posicion a y_wp
        y_wp.append(i[1])
    
    plt.figure()
    plt.scatter(x_wp,y_wp, marker='s',label='Waypoints (Metas)',color='k')      #utilizo un marker='s' para los puntos 
    plt.plot(x_ppo,y_ppo, label="Trayectoria PPO", linestyle='-', color='b')    #utilizo linestyle='-' para crear lineas continuas
    plt.plot(x_mask,y_mask, label='Trayectoria PPO-Mask', linestyle='--',color='r') #utilizo linestyle = '--' para crear lineas recortadas
    plt.xlabel("Posición X (metros)")
    plt.ylabel("Posición Y (metros)")
    plt.axis('equal')                                                           #utilizo el axis('equal') para que las unidades en x e y tengan la misma escala
    plt.grid()
    plt.legend()                                                                #genero leyenda para poder visualizarla en el grafico
    plt.title(f"Comparación de Navegación: Ruta {nombre}")
    
    os.makedirs("resultados_graficos", exist_ok=True)                           #Verifica que la carpeta resultado_graficos esté creada, si no lo está la crea                                                                       
    direccion = os.path.join("resultados_graficos",                             #Armo la direccion para guardar la figura 
                         f"trayectorias_{nombre}.png")            
    plt.savefig(direccion, dpi=300)                                             #Guardo la figura en la direccion creada con un dpi de 300 para tener resolucion alta

    plt.show()

    return
    

