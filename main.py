# import csv
# import os

# # Obtenemos la ruta absoluta del directorio actual
# directorio_actual = os.path.dirname(os.path.abspath(__file__))

# # Combinamos la ruta del directorio actual con el nombre del archivo CSV
# ruta_csv = os.path.join(directorio_actual, 'datos.csv')

# # Lista para almacenar los correos
# correos = []

# # Abrir el archivo CSV en modo lectura
# with open(ruta_csv, newline='', encoding='utf-8') as archivo_csv:
#     lector_csv = csv.DictReader(archivo_csv)

#     # Iterar sobre cada fila del archivo
#     for row in lector_csv:
#         correo = row["correo"]
#         correos.append(correo)

# # Filtrar solo los correos
# for correo in correos:
#     print(correo)

# # Contar el número de correos
# cantidad_correos = len(correos)
# print("Total de correos:", cantidad_correos)

import pandas as pd
# Leer el archivo CSV
datos = pd.read_csv('datos.csv')

# Extraer los correos
correos = datos['correo']

# Crear un DataFrame con los correos
df_correos = pd.DataFrame({'Correo': correos})

# Guardar los correos en un archivo Excel
df_correos.to_excel('correos.xlsx', index=False)

print("Los correos se han guardado en el archivo Excel correctamente.")
