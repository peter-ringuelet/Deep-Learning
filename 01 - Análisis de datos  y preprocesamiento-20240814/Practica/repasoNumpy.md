# Biblioteca Numpy

Numpy es una biblioteca especializada para cálculo numérico y análisis de datos. Permite representar, a través del tipo de datos array, colecciones de datos homogéneos (mismo tipo) en múltiples dimensiones y provee funciones eficientes para su manipulación. Para una referencia rápida puede acceder al video:  
https://www.youtube.com/watch?v=WxJr143Os-A

## Ejercicio 1

Practique la creación de vectores, matrices y tensores y responda:

- **¿Qué diferencias hay entre los constructores, array, empty, full, zeros, ones, identity?**

```bash
  # Ejemplos de constructores
  import numpy as np
  
  a = np.array([1, 2, 3])  # Crea un array con los valores proporcionados
  e = np.empty((2, 2))  # Crea un array sin inicializar valores (los valores serán aleatorios)
  f = np.full((2, 2), 7)  # Crea un array lleno con el valor 7
  z = np.zeros((2, 2))  # Crea un array lleno de ceros
  o = np.ones((2, 2))  # Crea un array lleno de unos
  i = np.identity(3)  # Crea una matriz identidad de 3x3
  
  print(a, e, f, z, o, i)
```

  **Diferencias**:  
  - `array`: Permite crear un array con los valores que se pasan como argumento.
  - `empty`: Crea un array sin inicializar los elementos, lo que significa que contendrá datos aleatorios.
  - `full`: Crea un array con un tamaño especificado, rellenándolo con un valor constante.
  - `zeros`: Crea un array lleno de ceros.
  - `ones`: Crea un array lleno de unos.
  - `identity`: Crea una matriz identidad (diagonal de unos y el resto ceros).

- **¿Qué tipos de datos pueden utilizarse? ¿En qué se diferencian? ¿Cuál es el tipo que se toma por defecto? ¿Es siempre el mismo?**

  **Tipos de datos**: Numpy soporta varios tipos de datos como `int`, `float`, `complex`, `bool`, `object`, `str`, entre otros.  
  **Diferencias**: Los tipos de datos varían en el tamaño y la precisión de los números que representan. Por ejemplo, `int32` y `int64` se diferencian en la cantidad de bits utilizados para almacenar el número.  
  **Tipo por defecto**: El tipo de dato por defecto depende de los datos que se proporcionan al crear el array. Si no se especifica un tipo, Numpy intenta inferirlo automáticamente, comúnmente como `float64` para números.

- **¿Qué funciones se pueden utilizar para generar arreglos con números aleatorios?**

```bash
  # Ejemplos de funciones para generar números aleatorios
  r1 = np.random.rand(3, 2)  # Crea un array de 3x2 con números aleatorios uniformemente distribuidos entre 0 y 1
  r2 = np.random.randint(0, 10, (3, 3))  # Crea un array de 3x3 con enteros aleatorios entre 0 y 9
  r3 = np.random.randn(3, 2)  # Crea un array de 3x2 con números aleatorios distribuidos normalmente (media 0 y desviación estándar 1)
  
  print(r1, r2, r3)
```

## Ejercicio 2

Investigue y ejemplifique las funciones relacionadas al tamaño de los arrays de Numpy:

- **¿Para qué sirven las funciones shape, len, ndim, size?**

```bash
  # Ejemplo de un array
  arr = np.array([[1, 2, 3], [4, 5, 6]])

  # Usos de shape, len, ndim, size
  print(arr.shape)  # Devuelve una tupla con las dimensiones del array (filas, columnas)
  print(len(arr))  # Devuelve el número de filas (primera dimensión)
  print(arr.ndim)  # Devuelve el número de dimensiones del array
  print(arr.size)  # Devuelve el número total de elementos en el array
```

  **Explicación**:  
  - `shape`: Devuelve las dimensiones del array como una tupla.
  - `len`: Devuelve el tamaño de la primera dimensión.
  - `ndim`: Devuelve el número de dimensiones del array.
  - `size`: Devuelve el número total de elementos en el array.

- **¿Qué tipos de datos pueden utilizarse? ¿En qué se diferencian? ¿Cuál es el tipo que se toma por defecto? ¿Es siempre el mismo?**

  *(Esta pregunta es redundante con la del Ejercicio 1, por lo que se refiere a la misma respuesta anterior.)*

- **¿Qué funciones se pueden utilizar para generar arreglos con números aleatorios?**

  *(Esta pregunta es redundante con la del Ejercicio 1, por lo que se refiere a la misma respuesta anterior.)*

## Ejercicio 3

Practique funciones de agregación (sum, min, max, etc.) sobre vectores, matrices y tensores. Enumere y pruebe todas las funciones que encuentre y responda:

```bash
# Ejemplo de un array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Funciones de agregación
print(np.sum(arr))  # Suma de todos los elementos
print(np.min(arr))  # Valor mínimo
print(np.max(arr))  # Valor máximo
print(np.mean(arr))  # Media
print(np.median(arr))  # Mediana
print(np.std(arr))  # Desviación estándar
print(np.prod(arr))  # Producto de todos los elementos
```

- **¿Estas funciones se aplican a todos los datos del array o pueden realizarse sobre dimensiones particulares? Ejemplifique.**

```bash
  # Ejemplo aplicando funciones sobre dimensiones particulares
  print(np.sum(arr, axis=0))  # Suma a lo largo de las columnas
  print(np.sum(arr, axis=1))  # Suma a lo largo de las filas
```

  **Explicación**: Estas funciones pueden aplicarse a todos los elementos del array o a lo largo de una dimensión particular utilizando el parámetro `axis`. Por ejemplo, `axis=0` aplica la función a lo largo de las columnas, mientras que `axis=1` lo hace a lo largo de las filas.

## Ejercicio 4

Investigue y realice ejemplos que utilicen funciones para manipular elementos de arreglos (append, insert, delete, etc.) y arreglos entre sí (vstack, hstack, concatenate, etc.)

```bash
# Ejemplos de manipulación de arreglos
arr = np.array([1, 2, 3, 4])

arr_appended = np.append(arr, 5)  # Agrega un elemento al final
arr_inserted = np.insert(arr, 1, 99)  # Inserta un elemento en la posición 1
arr_deleted = np.delete(arr, 2)  # Elimina el elemento en la posición 2

print(arr_appended)
print(arr_inserted)
print(arr_deleted)

# Ejemplos de manipulación entre arreglos
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

vstacked = np.vstack((arr1, arr2))  # Apila los arreglos verticalmente
hstacked = np.hstack((arr1, arr2))  # Apila los arreglos horizontalmente
concatenated = np.concatenate((arr1, arr2), axis=0)  # Concatenación a lo largo del eje 0

print(vstacked)
print(hstacked)
print(concatenated)
```

## Ejercicio 5

Los arrays de numpy (así como las listas) proveen de un mecanismo versátil para hacer o referenciar una sección de los mismos. Practique este mecanismo de acceso con vectores, matrices y tensores imprimiendo y modificando distintas regiones de los mismos.

```bash
# Ejemplo de slicing en un array
arr = np.array([10, 20, 30, 40, 50, 60])

# Slices
print(arr[1:4])  # Sublista desde el índice 1 al 4 (exclusivo)
print(arr[:3])  # Desde el inicio hasta el índice 3 (exclusivo)
print(arr[2:])  # Desde el índice 2 hasta el final
print(arr[::2])  # Slice con paso de 2

# Modificar una sección del array
arr[1:3] = [99, 88]
print(arr)
```
