from dominio import Dominio
import random
import csv

class DominioTSP(Dominio):

    """
    Esta clase modela el dominio del problema del Vendedor Viajero para su resolución
    con algoritmos probabilísticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar()
        Construye aleatoriamente una lista que representa una posible solución al problema.

    fcosto(sol)
        Calcula el costo asociado con una solución dada.

    vecino(sol)
        Calcula una solución vecina a partir de una solución dada.

    validar(sol)
        Valida que la solución dada cumple con los requisitos del problema.

    texto(sol)
        Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.
    """

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioTSP correctamente inicializada.
        """
        #Dominio.__init__(self, ciudades_rutacsv, ciudad_inicio)

        #Posible solucion, arreglar luego
        resultado = [] 
        with open(ciudades_rutacsv) as archivo_csv:
            archivo_lectura = csv.reader(archivo_csv) 
            for fila in archivo_lectura:
                resultado.append(fila[1:]) 
        nombre_ciudades = resultado.pop(0)
        self.ciudades = nombre_ciudades
        self.posicion_ciudad_inicio = ciudad_inicio
        self.costos = resultado

    def validar(self, sol):
        """Valida que la solución dada cumple con los requisitos del problema.

        Si n es el número de ciudades en el grafo, la solución debe:
        - Tener tamaño (n-1)
        - Contener sólo números enteros menores que n (las ciudades se numeran de 0 a (n-1))
        - No contener elementos repetidos
        - No contener la ciudad de inicio/fin del circuito

        Entradas:
        sol (list)
            La solución a validar.

        Salidas:
        (bool) True si la solución es válida, False en cualquier otro caso
        """

        # Pendiente: implementar este método
        for x in sol:
            if isinstance(x,int):
                print("La lista solo posee numeros enteros")
            else:
                print("La lista posee elementos que no son numeros enteros")

        pass

    def texto(self, sol):
        """Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

        La hilera cumple con el siguiente formato:
        Nombre ciudad inicio -> Nombre ciudad 1 -> ... -> Nombre ciudad n -> Nombre ciudad inicio

        Entradas:
        sol (list)
            Solución a representar como texto legible

        Salidas:
        (str) Hilera en el formato mencionado anteriormente.
        """

        # Pendiente: implementar este método
        pass

    def generar(self):
        """Construye aleatoriamente una lista que representa una posible solución al problema.

        Entradas:
        ninguna

        Salidas:
        (list) Una lista que representa una solución válida para esta instancia del vendedor viajero
        """
        

        datos = []
        for element in self.ciudades:
            datos.append(element)
        
        #quitar la ciudad de inicio
        datos.pop(datos.index(self.posicion_ciudad_inicio))
        
        #generar aleatorio
        sol=[]
        rango=len(datos)
        for i in range(rango):
            aux=random.randint(0,len(datos)-1)
            sol.append(aux)
            datos.pop(aux) 
        return sol
        

    def fcosto(self, sol):
        """Calcula el costo asociado con una solución dada.

        Entradas:
        sol (list)
            Solución cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solución
        """

        # Pendiente: implementar este método
        # pass
	
	#Posible implementacion, revisar luego
        costo = 0
        ciudad_actual = self.ciudades.index(self.posicion_ciudad_inicio)

        #Se recorre la solucion
        for i in sol:
            sumar=self.costos[int(i)][int(ciudad_actual)]
            costo=costo+float(sumar)
            ciudad_actual = i
          
        return costo

    def vecino(self, sol):
        """Calcula una solución vecina a partir de una solución dada.

        Una solución vecina comparte la mayor parte de su estructura con 
        la solución que la origina, aunque no son exactamente iguales. El 
        método transforma aleatoriamente algún aspecto de la solución
        original.

        Entradas:
        sol (list)
            Solución a partir de la cual se originará una nueva solución vecina

        Salidas:
        (list) Solución vecina
        """

        a=random.randint(0,len(sol)-2)
        sol[a], sol[a+1] = sol[a+1], sol[a]
        return sol
