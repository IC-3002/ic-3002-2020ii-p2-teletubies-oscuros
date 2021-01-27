import random
import math

def optimizar(dominio, temperatura = 10e32, tasa_enfriamiento = 0.95):
    """Algoritmo de optimización estocástica simulated annealing.

    Entradas:
    dominio (instancia de dominiotsp)
        Un objeto que modela el dominio del problema que se quiere aproximar.

    temperatura (float/int)
        Temperatura inicial del algoritmo, se recomienda un número alto

    tasa_enfriamiento (float)
        Porcentaje de enfriamiento de la temperatura durante cada iteración, el valor
        por defecto es 0.95, lo que indica una tasa de enfriamiento del 5%.

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """

    # implementacion:


    #se declara el arreglo que almacenara las ciudades
    ciudades = []
    #se llena el arreglo de ciudades
    ciudades = dominio.generar()
    #auxiliar de temperatura
    current_temp = temperatura
    #temperatura que define el final del algoritmo
    final_temp = 0.1
    #arreglo que expresaria la solucion de la funcion
    estados = []
    #arreglo que expresaria los costos de los estados de la funcion
    costos = []
    #selecciona el primer estado
    estado = ciudades[0]
    #se declara el costo del primer estado 
    costoEstado = fcosto(estado)
    #se agrega el estado al arreglo estados
    estados.append(estado)
    #se agrega el costo al arreglo costos
    costos.append(costo)
    #mientras la temperatura sea mayor que 0.1 el ciclo corre
    while current_temp > final_temp:
        #se declara un vecino nuevo y su costo
        vecino = random.choice(vecino(sol))
        costoVecino = fcosto(vecino)
        #validacion si este vecino es el mejor hasta ahora
        dif_costo = costoEstado - costoVecino
        #si la nueva solucion es la mejor, se acepta
        if dif_costo > 0:
            estados.append(vecino)
            costos.append(costoVecino)
            estado = vecino
            costoEstado = costoVecino
        #si la nueva solucion no es la mejor igual se acepta pero con una probabilidad de e**(diferencia del costo/temperatura actual)
        elif random.uniform(0,1) < math.exp(dif_costo/current_temp):
            estados.append(vecino)
            costos.append(costoVecino)
            estado = vecino
            costoEstado = costoVecino
        #bajar temperatura
        current_temp -= tasa_enfriamiento

    return estados
