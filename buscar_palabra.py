import os
import re

# Función para buscar una palabra en los archivos txt de la carpeta "data"
def buscar_palabra(palabra, carpeta):
    archivos_con_palabra = []
    for archivo in os.listdir(carpeta): #Se itera sobre los nombres de archivos
        if archivo.endswith(".txt"): #Se comprueba si el archivo tiene la extensión '.txt'
            #Se contruye la ruta completa del archivo carpeta\archivo
            ruta_archivo = os.path.join(carpeta, archivo) 

            #Abrir archivo en modo lectura (r) y codificacion utf-8 para caracteres especiales
            with open(ruta_archivo, "r", encoding="utf-8") as file:     
                #Lee el contenido completo del archivo y lo almacena en variable contenido
                contenido = file.read() 
                # Buscar la palabra en el contenido del archivo
                # escape escapa cualquier caracter especial que este dentro de la palabra
                # para que no sea tomada como metacaracter ej "foo.bar"
                # r'(?<![a-zA-Z_-])' (negative lookbehind assertion)
                # y r'(?![a-zA-Z_-])' (negative lookahead assertion) 
                # se aguran que la palabra se encuentre sola
                patron = r'(?<![a-zA-Z_-])' + re.escape(palabra) + r'(?![a-zA-Z_-])'

                #Se comprueba si hay coincidencia dentro del contenido
                if re.search(patron, contenido): 
                    # Una vez confirmado se agrega el nombre del archivo a la lista
                    archivos_con_palabra.append(archivo)
                    print(f"Palabra encontrada en el archivo: {archivo}")
    # Retorna la lista con los archivos en los que aparece la palabra
    return archivos_con_palabra

# Pedir al usuario que ingrese la palabra a buscar
palabra_a_buscar = input("Ingrese la palabra que desea buscar: ")

# Carpeta donde se encuentran los archivos txt
carpeta_data = "data"

# Buscar la palabra en los archivos txt de la carpeta "data"
archivos_encontrados = buscar_palabra(palabra_a_buscar, carpeta_data)

# Imprimir los archivos donde se encontró la palabra
# Se comprueba que la lista archivos_con_palabra tenga algo
if archivos_encontrados: 
    print("")
    print("Esa palabra aparece en los siguientes archivos:")
    for archivo in archivos_encontrados:
        print(archivo)
else:
    print("La palabra no se encontró en ningún archivo.")
