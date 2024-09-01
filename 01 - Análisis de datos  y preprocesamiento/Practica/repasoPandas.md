# Biblioteca Pandas

Pandas es un paquete de Python que proporciona estructuras de datos rápidas, flexibles y expresivas, diseñadas para trabajar con datos relacionales o etiquetados. Para comprender el objetivo de Pandas, puede revisar el video:  
https://www.youtube.com/watch?v=gimfTyCNfGw  
Para realizar los ejercicios prácticos, puede consultar el video:  
https://www.youtube.com/watch?v=5S01zSgE9GA.

## Ejercicio 1

Investigue el funcionamiento del Dataframe de Pandas y cree uno con la información de la siguiente tabla:

| Nombre | Edad | País       |
|--------|------|------------|
| Juan   | 20   | Argentina  |
| María  | 26   | Peru       |
| Pedro  | 18   | Brasil     |
| José   | 22   | Chile      |

Realice las siguientes operaciones:

- **Imprimir los nombres de las columnas.**

```bash
  import pandas as pd

  # Crear el DataFrame
  data = {'Nombre': ['Juan', 'María', 'Pedro', 'José'],
          'Edad': [20, 26, 18, 22],
          'País': ['Argentina', 'Peru', 'Brasil', 'Chile']}
  
  df = pd.DataFrame(data)

  # Imprimir los nombres de las columnas
  print(df.columns)
```

- **Agregar a la tabla a Pablo que tiene 30 años y es originario de Colombia. Agregarlo de 2 formas diferentes.**

```bash
  # Forma 1: Usar loc para agregar una nueva fila
  df.loc[len(df)] = ['Pablo', 30, 'Colombia']

  # Forma 2: Usar append para agregar una nueva fila
  df = df.append({'Nombre': 'Pablo', 'Edad': 30, 'País': 'Colombia'}, ignore_index=True)

  print(df)
```

- **Eliminar de la tabla al Pedro repetido.**

```bash
  # Identificar y eliminar filas duplicadas basadas en todas las columnas
  df = df.drop_duplicates()

  print(df)
```

- **Modificar los atributos de países que dicen “Peru” (sin acento) y reemplazarlos por “Perú” (con acento).**

```bash
  # Reemplazar "Peru" por "Perú"
  df['País'] = df['País'].replace('Peru', 'Perú')

  print(df)
```

## Ejercicio 2

Guarde en disco el dataframe del ejercicio anterior en los siguientes formatos:

- **Archivo con separación por delimitadores (tabulador como separador).**

```bash
  # Guardar en un archivo con tabulador como separador
  df.to_csv('data_tab.tsv', sep='\t', index=False)
```

- **Archivo con separación por delimitadores (punto y coma como separador).**

```bash
  # Guardar en un archivo con punto y coma como separador
  df.to_csv('data_puntoycoma.csv', sep=';', index=False)
```

- **Archivo Excel.**

```bash
  # Guardar en un archivo Excel
  df.to_excel('data.xlsx', index=False)
```

- **Archivo JSON.**

```bash
  # Guardar en un archivo JSON
  df.to_json('data.json', orient='records')
```
