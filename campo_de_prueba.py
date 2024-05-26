import os
import re
import inflect

def crear_matriz(carpeta):
    fila_palabras = []
    matriz = []
    columna_documentos = []

    inflect_engine = inflect.engine()
    
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            columna_documentos.append(archivo)
            print(archivo + "Primera Revision")
            ruta_archivo = os.path.join(carpeta, archivo)
            
            with open(ruta_archivo, "r", encoding="utf-8") as file:
                contenido = file.read().lower()
                
                # Utilizar expresión regular para extraer palabras
                palabras = re.findall(r'\b[a-zA-Z]+\b', contenido)
                
                # Singularizar y añadir a fila_palabras_temporal
                fila_palabras_temporal = set(inflect_engine.singular_noun(palabra) or palabra for palabra in palabras)
            
                # Singularizar y añadir a fila_palabras
                for palabra in palabras:
                    palabra_singular = inflect_engine.singular_noun(palabra) or palabra
                    if palabra_singular not in fila_palabras:
                        fila_palabras.append(palabra_singular)
    
    # Inicializar la matriz con ceros
    matriz = [[0 for _ in range(len(columna_documentos))] for _ in range(len(fila_palabras))]

    # Rellenar la matriz con la información de los documentos
    for col_idx, archivo in enumerate(columna_documentos):
        print(archivo + "Segunda Revision")
        ruta_archivo = os.path.join(carpeta, archivo)
        
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            contenido = file.read().lower()
            
            # Utilizar expresión regular para extraer palabras
            palabras = re.findall(r'\b[a-zA-Z]+\b', contenido)
            
            # Singularizar palabras
            palabras_singularizadas = set(inflect_engine.singular_noun(palabra) or palabra for palabra in palabras)
            
            # Actualizar la matriz para las palabras presentes en el documento actual
            for palabra in palabras_singularizadas:
                if palabra in fila_palabras:
                    fila_idx = fila_palabras.index(palabra)
                    matriz[fila_idx][col_idx] = 1
    
    return columna_documentos, fila_palabras, matriz

def buscar_palabra(consulta, columna_documentos, fila_palabras, matriz):
    inflect_engine = inflect.engine()
    
    def obtener_fila_palabra(palabra):
        palabra_singular = inflect_engine.singular_noun(palabra.lower()) or palabra.lower()
        if palabra_singular in fila_palabras:
            fila_idx = fila_palabras.index(palabra_singular)
            return matriz[fila_idx]
        else:
            return [0] * len(columna_documentos)
    
    def parsear_consulta(consulta):
        consulta = consulta.upper()
        tokens = re.split(r'\s+(AND|OR|NOT)\s+', consulta)
        return tokens

    def aplicar_operacion_logica(operacion, filas):
        if operacion == "AND":
            return list(map(int, map(all, zip(*filas))))
        elif operacion == "OR":
            return list(map(int, map(any, zip(*filas))))
        elif operacion == "NOT":
            return [1 - x for x in filas[0]]
        else:
            raise ValueError(f"Operación lógica desconocida: {operacion}")
    
    tokens = parsear_consulta(consulta)
    
    # Almacena filas según las palabras
    filas = []
    operaciones = []

    for token in tokens:
        if token in {"AND", "OR", "NOT"}:
            operaciones.append(token)
        else:
            filas.append(obtener_fila_palabra(token))
    
    # Aplica las operaciones lógicas
    while operaciones:
        operacion = operaciones.pop(0)
        if operacion == "NOT":
            fila = filas.pop(0)
            resultado = aplicar_operacion_logica(operacion, [fila])
            filas.insert(0, resultado)
        else:
            fila1 = filas.pop(0)
            fila2 = filas.pop(0)
            resultado = aplicar_operacion_logica(operacion, [fila1, fila2])
            filas.insert(0, resultado)
    
    # Convertir el resultado a nombres de documentos
    resultado_final = filas[0]
    documentos_presentes = [columna_documentos[col_idx] for col_idx, presente in enumerate(resultado_final) if presente == 1]
    
    return documentos_presentes

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

