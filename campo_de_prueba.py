import os
import re
import inflect

def crear_matriz(carpeta):
    fila_palabras = []
    matriz = []
    columna_documentos = []
    
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            columna_documentos.append(archivo)
            print(archivo)
            
            fila_palabras_temporal = set()
            ruta_archivo = os.path.join(carpeta, archivo)
            
            with open(ruta_archivo, "r", encoding="utf-8") as file:
                contenido = file.read().lower()
                
                # Dividir el contenido en palabras y eliminar caracteres no deseados
                eliminar = str.maketrans('', '', '.!?\'“”,:;_-"—[]{}‘’()')
                palabras = [palabra.translate(eliminar) for palabra in contenido.split()]
                
                # Iterar sobre cada palabra en la lista palabras
                inflect_engine = inflect.engine()
                for palabra in palabras:
                    if palabra:
                        palabra_singular = inflect_engine.singular_noun(palabra) or palabra
                        #print(palabra_singular + "\n")
                        fila_palabras_temporal.add(palabra_singular)
            
            # Agregar palabras únicas al conjunto global de palabras
            for palabra in fila_palabras_temporal:
                if palabra not in fila_palabras:
                    fila_palabras.append(palabra)
                    
            # Inicializar la fila de la matriz para el documento actual
            fila_actual = [1 if palabra in fila_palabras_temporal else 0 for palabra in fila_palabras]
            matriz.append(fila_actual)
    
    # Ajustar la matriz para que todas las filas tengan la misma longitud
    for fila in matriz:
        while len(fila) < len(fila_palabras):
            fila.append(0)
    
    return columna_documentos, fila_palabras, matriz

def buscar_palabra(ejey_documentos, ejex_palabras, matriz, palabra_a_buscar, carpeta):
    archivos = []
    archivos_con_palabra = []
    
    palabra_a_buscar = palabra_a_buscar.lower()

    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            archivos.append(archivo)

    if palabra_a_buscar in ejex_palabras:
        indice_palabra = ejex_palabras.index(palabra_a_buscar)
        
        for i, documento in enumerate(ejey_documentos):
            if matriz[i][indice_palabra] == 1:
                archivos_con_palabra.append(documento)
    
    return archivos_con_palabra

# Carpeta donde se encuentran los archivos txt
carpeta_data = "data_muestra"

# Realizar diccionario con la matriz binaria
columnas_doc, fila_palabras, matriz_binaria = crear_matriz(carpeta_data)

# # Imprimir la lista de palabras únicas
# print("Palabras únicas:")
# print(fila_palabras)

# # Imprimir los nombres de los documentos
# print("Documentos:")
# print(columnas_doc)

# # Imprimir la matriz
# print("Matriz:")
# for fila in matriz_binaria:
#     print(fila)

# print(matriz_binaria)

# Pedir al usuario que ingrese la palabra a buscar
palabra_a_buscar = input("Ingrese la palabra que desea buscar: ")

#Realizar busqueda
archivos_encontrados = buscar_palabra(columnas_doc, fila_palabras, matriz_binaria, palabra_a_buscar, carpeta_data)

# Se comprueba que la lista archivos_con_palabra tenga algo
if archivos_encontrados: 
    print("")
    print("Esa palabra aparece en los siguientes archivos:")
    for archivo in archivos_encontrados:
        print(archivo)
else:
    print("La palabra no se encontró en ningún archivo.")
