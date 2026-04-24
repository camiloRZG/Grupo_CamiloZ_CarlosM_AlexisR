def cargar_experimentos(): #definimos una funcion para la creacion de un diccionario
    datos={
        "exp1":{"politica":"PPO",  "ambiente":"Real",  "ruta":"simple", "ISE":434.99, "IAE":135.93,  "ITSE":6932.79,  "ITAE":2601.61, "tiempo":None, "pasos":None, "reward_medio":None
              },
        "exp2":{"politica":"PPO-Mask",  "ambiente":"Real",  "ruta":"simple", "ISE":362.85, "IAE":128.92,  "ITSE":5869.30,  "ITAE":2669.86, "tiempo":None, "pasos":None, "reward_medio":None 
              },
        "exp3":{"politica":"PPO",  "ambiente":"Simulated",  "ruta":"simple", "ISE":73.35, "IAE":24.51,  "ITSE":203.90,  "ITAE":89.73, "tiempo":None, "pasos":None, "reward_medio":None 
              },
        "exp4":{"politica":"PPO-Mask",  "ambiente":"Simulated",  "ruta":"simple", "ISE":73.79, "IAE":22.91,  "ITSE":200.16,  "ITAE":73.77, "tiempo":None, "pasos":None, "reward_medio":None 
              },
        "exp5":{"politica":"PPO",  "ambiente":"Simulated",  "ruta":"Square", "ISE":None, "IAE":None,  "ITSE":None,  "ITAE":None, "tiempo":27.89, "pasos":270, "reward_medio":7.12 
              },
        "exp6":{"politica":"PPO",  "ambiente":"Real",  "ruta":"Square", "ISE":None, "IAE":None,  "ITSE":None,  "ITAE":None, "tiempo":112.48, "pasos":594, "reward_medio":3.15
              },
        "exp7":{"politica":"PPO-Mask",  "ambiente":"Simulated",  "ruta":"Square", "ISE":None, "IAE":None,  "ITSE":None,  "ITAE":None, "tiempo":24.42, "pasos":235, "reward_medio":7.94 
              },
        "exp8":{"politica":"PPO-Mask",  "ambiente":"Real",  "ruta":"Square", "ISE":None, "IAE":None,  "ITSE":None,  "ITAE":None, "tiempo":103.46, "pasos":569, "reward_medio":4.13 
              },
        "exp9":{"politica":"PPO",  "ambiente":"Simulated",  "ruta":"Triangular", "ISE":None, "IAE":None,  "ITSE":None,  "ITAE":None, "tiempo":26.20, "pasos":254, "reward_medio":7.38 
              },
        "exp10":{"politica":"PPO",  "ambiente":"Real",  "ruta":"Triangular", "ISE":None, "IAE":None,  "ITSE":None,  "ITAE":None, "tiempo":104.37, "pasos":581, "reward_medio":3.92
              },
        "exp11":{"politica":"PPO-Mask",  "ambiente":"Simulated",  "ruta":"Triangular", "ISE":None, "IAE":None,  "ITSE":None,  "ITAE":None, "tiempo":22.75, "pasos":219, "reward_medio":8.25 
              },
        "exp12":{"politica":"PPO-Mask",  "ambiente":"Real",  "ruta":"Triangular", "ISE":None, "IAE":None,  "ITSE":None,  "ITAE":None, "tiempo":116.71, "pasos":638, "reward_medio":4.45 
              },
              
    }
    return datos
mis_experimentos = cargar_experimentos()
print(mis_experimentos)
       



       
#parte2B
import numpy as np
import matplotlib as plt

def generar_trayectoria_ideal(waypoints, puntos_por_segmento=100): #definimos funcion para la parte b
    x_ideal = [] #contiene cords en eje x
    y_ideal = [] #contiene cords en eje y
    for i in range(len(waypoints)-1): #ciclo for para leer el vector de los waypoinst
     valores_iniciales_x= waypoints[i][0] #generamos variable para que reconosca nuestro ejex 
     valores_iniciales_y=waypoints[i][1] #generamos variable para que reconosca nuestro ejey 
     valores_finales_x=waypoints[i+1][0] #Damos stop en x  al momento de llegar al final del vector
     valores_finales_y=waypoints[i+1][1] #Damos stop en y al momento de llegar al final del vector
     valores_intermedios_x=np.linspace(valores_iniciales_x, valores_finales_x, puntos_por_segmento ) #generamos la cantidad de puntos con linspace
     valores_intermedios_y=np.linspace(valores_iniciales_y, valores_finales_y, puntos_por_segmento) #generamos la cantidad de puntos con linspace
     x_ideal.extend(valores_intermedios_x) #ordenamos y empaquetamos con extend todos los puntos del arreglo
     y_ideal.extend(valores_intermedios_y) #ordenamos y empaquetamos con extend todos los puntos del arreglo

    return np.array(x_ideal), np.array(y_ideal)



#parte2C
import numpy as np
import matplotlib.pyplot as plt 

def simular_lidar(n_sectores=36, d_min=0.5, d_max=30.0):
    angulos = np.linspace(0, 360, n_sectores) #Genera ángulos de 0 a 360 grados
    distancias = np.random.uniform(d_min, d_max, n_sectores) #Genera distancias aleatorias uniformes
    distancias[5:9] = np.random.uniform(0.5, 2.0, 4) #Inserta obstáculo en sectores 5 al 8
    distancias_normalizadas = (distancias - d_min) / (d_max - d_min)  #Normaliza distancias entre 0 y 1
    return angulos, distancias, distancias_normalizadas #Retorna los tres arreglos
    

    