import time

# Función de complejidad lineal O(n)
def funcion_lineal(n):
    resultado = 0
    for i in range(n):
        resultado += i
    return resultado

# Medir tiempos de ejecución con distintos valores de n
def medir_tiempos_funcion_lineal(valores_n):
    tiempos = []
    for n in valores_n:
        inicio = time.time()
        funcion_lineal(n)
        fin = time.time()
        tiempos.append((n, fin - inicio))

    return tiempos

# Ejecución y muestra de resultados
arrValN=[10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
resultados = medir_tiempos_funcion_lineal(arrValN)
for n, tiempo in resultados:
    print(f"n={n:<10} tiempo={tiempo:.6f} segundos")

# Función de complejidad logarítmica O(log n)
def funcion_logaritmica(n):
    resultado = 0
    while n > 1:
        resultado += n
        n //= 2
    return resultado
# Medir tiempos de ejecución con valores incrementales de n
def medir_tiempos_funcion_logaritmica(valores_n):
    tiempos = []
    for n in valores_n:
        inicio = time.time()
        funcion_logaritmica(n)
        fin = time.time()
        tiempos.append((n, fin - inicio))

    return tiempos
# Ejecución y muestra de resultados
resultados_logaritmicos = medir_tiempos_funcion_logaritmica([10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000])
for n, tiempo in resultados_logaritmicos:
    print(f"n={n}, tiempo={tiempo:.6f} segundos")
# Función de complejidad cuadrática O(n^2)
def funcion_cuadratica(n):
    resultado = 0
    for i in range(n):
        for j in range(n):
            resultado += i * j
    return resultado
# Medir tiempos de ejecución con valores incrementales de n
def medir_tiempos_funcion_cuadratica(valores_n):
    tiempos = []
    for n in valores_n:
        inicio = time.time()
        funcion_cuadratica(n)
        fin = time.time()
        tiempos.append((n, fin - inicio))

    return tiempos
# Ejecución y muestra de resultados
resultados_cuadraticos = medir_tiempos_funcion_cuadratica([10, 100, 1000, 10000, 100000])
for n, tiempo in resultados_cuadraticos:
    print(f"n={n}, tiempo={tiempo:.6f} segundos")
# Función de complejidad cúbica O(n^3)
def funcion_cubica(n):
    resultado = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado += i * j * k
    return resultado
# Medir tiempos de ejecución con valores incrementales de n
def medir_tiempos_funcion_cubica(valores_n):
    tiempos = []
    for n in valores_n:
        inicio = time.time()
        funcion_cubica(n)
        fin = time.time()
        tiempos.append((n, fin - inicio))

    return tiempos
# Ejecución y muestra de resultados
resultados_cubicos = medir_tiempos_funcion_cubica([10, 100, 1000])
for n, tiempo in resultados_cubicos:
    print(f"n={n}, tiempo={tiempo:.6f} segundos")


    # Función de complejidad O(n log n)
    def funcion_n_log_n(n):
        resultado = 0
        for i in range(n):
            m = n
            while m > 1:
                resultado += i
                m //= 2
        return resultado

    # Medir tiempos de ejecución con valores incrementales de n
    def medir_tiempos_funcion_n_log_n(valores_n):
        tiempos = []
        for n in valores_n:
            inicio = time.time()
            funcion_n_log_n(n)
            fin = time.time()
            tiempos.append((n, fin - inicio))

        return tiempos

    # Ejecución y muestra de resultados
    resultados_n_log_n = medir_tiempos_funcion_n_log_n([10, 100, 1000, 10000, 100000])
    for n, tiempo in resultados_n_log_n:
        print(f"n={n}, tiempo={tiempo:.6f} segundos")


# Función de complejidad exponencial O(2^n)
def funcion_exponencial(n):
    if n == 0:
        return 1
    else:
        return 2 * funcion_exponencial(n - 1)
# Medir tiempos de ejecución con valores incrementales de n
def medir_tiempos_funcion_exponencial(valores_n):
    tiempos = []
    for n in valores_n:
        inicio = time.time()
        funcion_exponencial(n)
        fin = time.time()
        tiempos.append((n, fin - inicio))

    return tiempos
# Ejecución y muestra de resultados
resultados_exponenciales = medir_tiempos_funcion_exponencial([10, 20, 30])  # Cambia estos valores para probar con diferentes tamaños  
for n, tiempo in resultados_exponenciales:
    print(f"n={n}, tiempo={tiempo:.6f} segundos")
# Función de complejidad factorial O(n!)
def funcion_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * funcion_factorial(n - 1)
# Medir tiempos de ejecución con valores incrementales de n
def medir_tiempos_funcion_factorial(valores_n):
    tiempos = []
    for n in valores_n:
        inicio = time.time()
        funcion_factorial(n)
        fin = time.time()
        tiempos.append((n, fin - inicio))

    return tiempos
# Ejecución y muestra de resultados
resultados_factoriales = medir_tiempos_funcion_factorial([5, 6, 7])  # Cambia estos valores para probar con diferentes tamaños
for n, tiempo in resultados_factoriales:
    print(f"n={n}, tiempo={tiempo:.6f} segundos")
# Función de complejidad constante O(1)
def funcion_constante():
    return 42  # Valor constante
# Medir tiempos de ejecución con valores incrementales de n 
def medir_tiempos_funcion_constante(valores_n):
    tiempos = []
    for n in valores_n:
        inicio = time.time()
        funcion_constante()
        fin = time.time()
        tiempos.append((n, fin - inicio))

    return tiempos
# Ejecución y muestra de resultados
resultados_constantes = medir_tiempos_funcion_constante([10, 100, 1000, 10000, 100000])
for n, tiempo in resultados_constantes:
    print(f"n={n}, tiempo={tiempo:.6f} segundos")
