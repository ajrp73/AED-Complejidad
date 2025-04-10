import time

def inicializar_array(array):
    # Rellena el array con valores 1 usando un bucle for
    for i in range(len(array)):
        array[i] = 1
    return array

# Crear un array vacío de tamaño n
n = 10  # Cambia este valor para probar con diferentes tamaños
array = [0] * n  # Inicialmente lleno de ceros

# Medir el tiempo antes y después de la llamada a la función
inicio = time.time()  # Tiempo antes de la llamada
array_inicializado = inicializar_array(array)
fin = time.time()  # Tiempo después de la llamada

# Calcular el tiempo invertido
tiempo_invertido = fin - inicio
print("Array inicializado:", array_inicializado)
print("Tiempo invertido:", tiempo_invertido, "segundos")
