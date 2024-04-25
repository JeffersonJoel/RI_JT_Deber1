import os
import re

# Función para buscar una palabra en los archivos txt de la carpeta "data"
def buscar_palabra(palabra, carpeta):
    archivos_con_palabra = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            ruta_archivo = os.path.join(carpeta, archivo)
            with open(ruta_archivo, "r", encoding="utf-8") as file:
                contenido = file.read()
                # Buscar la palabra en el contenido del archivo
                patron = r'(?<![a-zA-Z_-])' + re.escape(palabra) + r'(?![a-zA-Z_-])'
                if re.search(patron, contenido):
                    archivos_con_palabra.append(archivo)
                    print(f"Palabra encontrada en el archivo: {archivo}")
    return archivos_con_palabra

# Pedir al usuario que ingrese la palabra a buscar
palabra_a_buscar = input("Ingrese la palabra que desea buscar: ")

# Carpeta donde se encuentran los archivos txt
carpeta_data = "data"

# Buscar la palabra en los archivos txt de la carpeta "data"
archivos_encontrados = buscar_palabra(palabra_a_buscar, carpeta_data)

# Imprimir los archivos donde se encontró la palabra
if archivos_encontrados:
    print("")
    print("Esa palabra aparece en los siguientes archivos:")
    for archivo in archivos_encontrados:
        print(archivo)
else:
    print("La palabra no se encontró en ningún archivo.")
