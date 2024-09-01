import numpy as np
# Ejemplo de diccionario
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Recorrer el diccionario e imprimir sus valores
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

 # Ejemplo de un array
arr = np.array([[1, 2, 3], [4, 5, 6]])

  # Usos de shape, len, ndim, size
print(arr.shape)  # Devuelve una tupla con las dimensiones del array (filas, columnas)
print(len(arr))  # Devuelve el número de filas (primera dimensión)
print(arr.ndim)  # Devuelve el número de dimensiones del array
print(arr.size)  # Devuelve el número total de elementos en el array

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

 # Ejemplo aplicando funciones sobre dimensiones particulares
print(np.sum(arr, axis=0))  # Suma a lo largo de las columnas
print(np.sum(arr, axis=1))  # Suma a lo largo de las filas

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

import pandas as pd

  # Crear el DataFrame
data = {'Nombre': ['Juan', 'María', 'Pedro', 'José'],
        'Edad': [20, 26, 18, 22],
        'País': ['Argentina', 'Peru', 'Brasil', 'Chile']}
  
df = pd.DataFrame(data)

  # Imprimir los nombres de las columnas
print(df.columns)

  # Guardar en un archivo con tabulador como separador
df.to_csv('data_tab.tsv', sep='\t', index=False)
print('exito')