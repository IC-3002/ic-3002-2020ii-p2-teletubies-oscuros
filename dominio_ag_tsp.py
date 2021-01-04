from dominio_ag import DominioAG
from dominio_tsp import DominioTSP
import random

class DominioAGTSP(DominioAG, DominioTSP):
    """
    Representa el objeto de dominio que conoce los detalles de implementación y modelamiento
    del problema del vendedor viajero para ser resuelto con algoritmos genéticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar(n)
        Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

    cruzar(sol_a, sol_b)
        Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

    mutar(sol)
        Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.
    """

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero para ser resuelto
        con algoritmos genéticos.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioAGTSP correctamente inicializada.
        """
        
        # Pendiente: implementar este constructor
        pass

    def generar_n(self, n):
        """Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

        Entradas:
        n (int)
            Número de soluciones aleatorias a generar.

        Salidas:
        (list) Lista que contiene n listas, cada una representando
        una posible solución al problema modelado por el objeto de dominio.
        """
        
        # Pendiente: implementar este método
        pass

    def cruzar(self, sol_a, sol_b):
        """Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

        Entradas:
        sol_a (estructura de datos)
            Estructura de datos que modela la solución antecesora A que será cruzada con la B

        sol_b (estructura de datos)
            Estructura de datos que modela la solución antecesora B que será cruzada con la A

        Salidas:
        (estructura de datos) Una nueva solución producto del cruzamiento entre las soluciones A y B
        """

        # IMPLEMENTACION 
        
        """
        OBTENER EL PUNTO DE CRUCE:
            se obtiene un random de 1 a len(sol)-2 para evitar puntos de cruze 
            en los extremos de la cadena
        """
        puntoCruce = random.randint(1, len(sol_a)-2)
        
        hijo=[]
        
        #Elegir cual solucion va primero en el cruce
        if(random.randint(0,1)==0):
            for i in range(puntoCruce):
                hijo.append(sol_a[i])
            for i in range(puntoCruce, len(sol_a)):
                hijo.append(sol_b[i])
        else:
            for i in range(puntoCruce):
                hijo.append(sol_b[i])
            for i in range(puntoCruce, len(sol_a)):
                hijo.append(sol_a[i])
                
        return hijo

    def mutar(self, sol):
        """Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.

        Entradas:
        sol (estructura de datos)
            La solución a mutar.
        
        Salidas:
        (estructura de datos) Una nueva solución que refleja un ligero cambio con respecto 
        a la solución dada por parámetro
        """

        # IMPLEMENTACION
        
        """
        MUTACION DE INTERCAMBIO:
            se eligen 2 indices aleatorios y se intercambian sus valores
        """
        index1 = random.randint(0,len(sol))
        index2 = random.randint(0,len(sol))
        num1=sol[index1]
        
        sol[index1] = sol[index2]
        sol[index2] = num1
        
        return sol