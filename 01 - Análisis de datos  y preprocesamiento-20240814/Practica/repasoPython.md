# Ejercicios de Python

## Ejercicio 1: Listas, Tuplas, Conjuntos y Diccionarios

### Listas
Las listas son colecciones ordenadas y mutables de elementos. Pueden contener elementos de diferentes tipos.

```bash
# Ejemplo de lista
mi_lista = [1, 2, 3, 4, 5]

# Recorrer la lista e imprimir sus valores
for elemento in mi_lista:
    print(elemento)
```

### Tuplas
Las tuplas son colecciones ordenadas e inmutables. Una vez creada, no se pueden modificar.

```bash
# Ejemplo de tupla
mi_tupla = (1, 2, 3, 4, 5)

# Recorrer la tupla e imprimir sus valores
for elemento in mi_tupla:
    print(elemento)
```

### Conjuntos
Los conjuntos son colecciones no ordenadas y sin elementos duplicados.

```bash
# Ejemplo de conjunto
mi_conjunto = {1, 2, 3, 4, 5}

# Recorrer el conjunto e imprimir sus valores
for elemento in mi_conjunto:
    print(elemento)
```

### Diccionarios
Los diccionarios son colecciones de pares clave-valor, desordenados y mutables.

```bash
# Ejemplo de diccionario
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Recorrer el diccionario e imprimir sus valores
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")
```

## Ejercicio 2: Recorrer dos listas simultáneamente con `zip`

```bash
# Ejemplo de dos listas
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

# Recorrer ambas listas simultáneamente
for elemento1, elemento2 in zip(lista1, lista2):
    print(f"Elemento de lista1: {elemento1}, Elemento de lista2: {elemento2}")
```

## Ejercicio 3: Función para eliminar elementos duplicados en una lista

```bash
def eliminar_duplicados(lista):
    # Convertir la lista en un conjunto para eliminar duplicados y luego convertir de nuevo en lista
    return list(set(lista))

# Ejemplo de uso
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = eliminar_duplicados(lista_con_duplicados)
print(lista_sin_duplicados)
```

## Ejercicio 4: Función para calcular la distancia entre dos puntos (2D)

```bash
import math

def calcular_distancia(punto1, punto2):
    # Calcular la distancia utilizando la fórmula de la distancia euclidiana
    return math.sqrt((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)

# Ejemplo de uso
puntoA = (1, 2)
puntoB = (4, 6)
distancia = calcular_distancia(puntoA, puntoB)
print(f"La distancia entre {puntoA} y {puntoB} es {distancia}")
```

## Ejercicio 5: Slices en listas

Los slices permiten obtener sublistas a partir de una lista original, especificando un rango de índices.

```bash
# Ejemplo de lista
mi_lista = [10, 20, 30, 40, 50, 60]

# Obtener un slice desde el índice 1 al 4 (exclusivo)
sublista = mi_lista[1:4]
print(sublista)  # Salida: [20, 30, 40]

# Obtener un slice desde el inicio hasta el índice 3 (exclusivo)
sublista = mi_lista[:3]
print(sublista)  # Salida: [10, 20, 30]

# Obtener un slice desde el índice 2 hasta el final
sublista = mi_lista[2:]
print(sublista)  # Salida: [30, 40, 50, 60]

# Obtener un slice con un paso de 2
sublista = mi_lista[::2]
print(sublista)  # Salida: [10, 30, 50]
```
