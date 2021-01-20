import random
import math

def optimizar(dominio, temperatura = 10e32, tasa_enfriamiento = 0.95):
    """Algoritmo de optimización estocástica simulated annealing.

    Entradas:
    dominio (Dominio)
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

    # Pendiente: implementar esta función
    initial s = 0 #corregir esta linea

    current_temp = temperatura

    current s = s_inicial

    solucion = current_s

    while temperatura > current_temp:
        vecinoNuevo = random.choice(vecino(self,sol))

        #validacion si este vecino es el mejor hasta ahora
        dif_costo = fcosto(self.current_s) = fcosto(vecinoNuevo)
        #si la nueva solucion es mejor, se acepta
        if dif_costo > 0:
            solucion = vecinoNuevo
        else:
            if random.uniform(0,1) < math.exp(dif_costo/current_temp):
                solucion = vecinoNuevo
        #bajar temperatura
        current_temp -= tasa_enfriamiento

    return solucion
