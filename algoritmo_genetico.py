import math
import random

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

    # Pendiente: implementar este método    FALTA LO DE LA APTITUD
    poblacion = dominio.generar_n(tam_pobl)
    while reps > 0: 
        for solucion in poblacion: 
            solucion.aptitud = dominio.fcosto(solucion)
        orderarAptitud(poblacion)
        num_padres = math.floor(len(poblacion)*porc_elite)
        num_hijos = len(poblacion) - num_padres
        sig_geneneracion = poblacion[0:num_padres]
        descendencia=[]
        while num_hijos > 0:
            padre_A = sig_geneneracion[random.randint(0,len(sig_geneneracion)-1)]
            padre_B = sig_geneneracion[random.randint(0,len(sig_geneneracion)-1)]
            hijo = dominio.cuzar(padre_A,padre_B)
            if (random.randint(0,100) < prob_mut*100):
                hijo = dominio.mutar(hijo)
            descendencia.append(hijo)
            num_hijos -= 1
        sig_geneneracion.append(descendencia)
        poblacion=sig_geneneracion
        reps -= 1