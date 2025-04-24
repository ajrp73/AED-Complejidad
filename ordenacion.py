# El algoritmo de ordenación por burbuja es un algoritmo de ordenación simple que compara elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que el array está ordenado.
import random
import time
def ordenacion_burbuja(array):
    """
    Ordena un array de números usando el algoritmo de ordenación por burbuja.

    :param array: Lista de números a ordenar.
    :return: Lista ordenada de menor a mayor.
    """
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                array[j], array[j+1] = array[j+1], array[j]
    return array

def medir_tiempos_casos_ordenacion_burbuja(longitudes):
    """
    Mide los tiempos de ordenación por burbuja para el mejor caso, peor caso y caso medio.

    :param longitudes: Lista de longitudes de los arrays a generar.
    :return: Diccionario con claves 'mejor_caso', 'peor_caso', 'medio_caso' y valores como listas de tiempos para cada longitud.
    """
    tiempos = {
        'mejor_caso': [],
        'peor_caso': [],
        'medio_caso': []
    }
    for longitud in longitudes:
        # Crear un array aleatorio de la longitud especificada
        array = [random.randint(0, 100) for _ in range(longitud)]
        
        # Mejor caso: array ya ordenado
        array_mejor = sorted(array)
        inicio = time.time()
        ordenacion_burbuja(array_mejor)
        fin = time.time()
        tiempos['mejor_caso'].append(fin - inicio)

        # Peor caso: array ordenado inversamente
        array_peor = sorted(array, reverse=True)
        inicio = time.time()
        ordenacion_burbuja(array_peor)
        fin = time.time()
        tiempos['peor_caso'].append(fin - inicio)

        # Caso medio: array aleatorio
        array_medio = array[:]
        inicio = time.time()
        ordenacion_burbuja(array_medio)
        fin = time.time()
        tiempos['medio_caso'].append(fin - inicio)
    
    return tiempos


def ordenación_quicksort(array):
            """
            Ordena un array de números usando el algoritmo quicksort y explica cada paso.

            :param array: Lista de números a ordenar.
            :return: Lista ordenada de menor a mayor.
            """
            if len(array) <= 1:
                # Si el array tiene 0 o 1 elementos, ya está ordenado
                return array
            else:
                # Elegir el pivote como el elemento central
                pivot = array[len(array) // 2]
                               
                # Dividir el array en tres partes: menores, iguales y mayores
                menores = [x for x in array if x < pivot]
                iguales = [x for x in array if x == pivot]
                mayores = [x for x in array if x > pivot]
                
                #print(f"Elementos menores que el pivote {pivot}: {menores}")
                #print(f"Elementos iguales al pivote {pivot}: {iguales}")
                #print(f"Elementos mayores que el pivote {pivot}: {mayores}")
                
                # Recursivamente ordenar las partes menores y mayores
                return ordenación_quicksort(menores) + iguales + ordenación_quicksort(mayores)


def medir_tiempos_casos_ordenacion_quicksort(longitudes):
    """
    Mide los tiempos de ordenación por quicksort para el mejor caso, peor caso y caso medio.

    :param longitudes: Lista de longitudes de los arrays a generar.
    :return: Diccionario con claves 'mejor_caso', 'peor_caso', 'medio_caso' y valores como listas de tiempos para cada longitud.
    """
    tiempos = {
        'mejor_caso': [],
        'peor_caso': [],
        'medio_caso': []
    }
    for longitud in longitudes:
        # Crear un array aleatorio de la longitud especificada
        array = [random.randint(0, 100) for _ in range(longitud)]
        
        if longitud == 10 or longitud == 100:
            print(f"Array original: {array}")   

        # Mejor caso: array ya ordenado
        array_mejor = sorted(array)
        inicio = time.time()
        ordenación_quicksort(array_mejor)
        fin = time.time()
        tiempos['mejor_caso'].append(fin - inicio)

        # Peor caso: array ordenado inversamente
        array_peor = sorted(array, reverse=True)
        inicio = time.time()
        ordenación_quicksort(array_peor)
        fin = time.time()
        tiempos['peor_caso'].append(fin - inicio)

        # Caso medio: array aleatorio
        array_medio = array[:]
        inicio = time.time()
        ao= ordenación_quicksort(array_medio)
        fin = time.time()
        tiempos['medio_caso'].append(fin - inicio)

        if longitud == 10 or longitud == 100:
            print(f"Array ordenado: {ao}") 
    
    return tiempos


longitudes = [10, 100, 1000, 10000]

tiempos_burbuja = medir_tiempos_casos_ordenacion_burbuja(longitudes)

# Mostrar los tiempos obtenidos para la ordenación por burbuja

print("Tiempos de búsqueda lineal:")
print(f"{'Longitud':<15}{'Mejor caso':<15}{'Caso medio':<15}{'Peor caso':<15}")
print("-" * 60)
for i, longitud in enumerate(longitudes):
    print(f"{longitud:<15}{tiempos_burbuja['mejor_caso'][i]:<15.6f}{tiempos_burbuja['medio_caso'][i]:<15.6f}{tiempos_burbuja['peor_caso'][i]:<15.6f}")

    tiempos_quicksort = medir_tiempos_casos_ordenacion_quicksort(longitudes)

    # Mostrar los tiempos obtenidos para la ordenación por quicksort
    print("\nTiempos de ordenación quicksort:")
    print(f"{'Longitud':<15}{'Mejor caso':<15}{'Caso medio':<15}{'Peor caso':<15}")
    print("-" * 60)
    for i, longitud in enumerate(longitudes):
        print(f"{longitud:<15}{tiempos_quicksort['mejor_caso'][i]:<15.6f}{tiempos_quicksort['medio_caso'][i]:<15.6f}{tiempos_quicksort['peor_caso'][i]:<15.6f}")