import math
import random
import numpy as np 

def optimizar(dominio, tam_pobl, porc_elite, prob_mut, reps):
    """Algoritmo genético para optimización estocástica.

    Entradas:
    dominio ( instancia dominio_ag_tsp)
        Un objeto que modela el dominio del problema que se quiere aproximar.
    
    tam_pobl (int)
        Tamaño de la población.
    
    porc_elite (float)
        Porcentaje de la población que se tomará como elite.
    
    prob_mut (float)
        Probabilidad de mutación, debe estar en el rango [0, 1]
    
    reps (int)
        Número de iteraciones a ejecutar.

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """

    # Implementacion
    poblacion = dominio.generar_n(tam_pobl)
    while reps > 0: 
        aux_poblacion = []
        for solucion in poblacion: 
            aux_poblacion.append((solucion, dominio.fcosto(solucion)))
        poblacion=ordenarAptitud(aux_poblacion)
        num_padres = math.floor(len(poblacion)*porc_elite)
        num_hijos = len(poblacion) - num_padres
        sig_geneneracion = poblacion[0:num_padres]
        descendencia=[]
        while num_hijos > 0:
            aux_padres=sig_geneneracion
            padre_A = sig_geneneracion[random.randint(0,len(sig_geneneracion)-1)] #tomar uno aleatorio de la poblacion ya seleccionada
            aux_padres.pop(padre_A)
            padre_B = aux_padres[random.randint(0,len(sig_geneneracion)-1)]
            hijo = dominio.cuzar(padre_A,padre_B)
            if (np.random.normal(0.0, 1.0) < prob_mut):      #cambiar a random con dist normal
                hijo = dominio.mutar(hijo)
            descendencia.append(hijo)
            num_hijos -= 1
        sig_geneneracion.append(descendencia)
        poblacion=sig_geneneracion
        reps -= 1
    return poblacion
    
def ordenarAptitud(aux_poblacion):
    poblacion=[]
    aux_poblacion=sorted(aux_poblacion, key=lambda x: x[1])
    for tupla in aux_poblacion:
        poblacion.append(tupla[0])
    return poblacion
