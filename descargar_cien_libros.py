import requests
import os

# Lista de enlaces
enlaces = [
    "https://www.gutenberg.org/cache/epub/84/pg84.txt",
"https://www.gutenberg.org/cache/epub/1342/pg1342.txt",
"https://www.gutenberg.org/cache/epub/2701/pg2701.txt",
"https://www.gutenberg.org/cache/epub/1513/pg1513.txt",
"https://www.gutenberg.org/cache/epub/16594/pg16594.txt",
"https://www.gutenberg.org/cache/epub/145/pg145.txt",
"https://www.gutenberg.org/cache/epub/21765/pg21765.txt",
"https://www.gutenberg.org/cache/epub/2542/pg2542.txt",
"https://www.gutenberg.org/cache/epub/844/pg844.txt",
"https://www.gutenberg.org/cache/epub/2641/pg2641.txt",
"https://www.gutenberg.org/cache/epub/100/pg100.txt",
"https://www.gutenberg.org/cache/epub/37106/pg37106.txt",
"https://www.gutenberg.org/cache/epub/11/pg11.txt",
"https://www.gutenberg.org/cache/epub/2581/pg2581.txt",
"https://www.gutenberg.org/cache/epub/64317/pg64317.txt",
"https://www.gutenberg.org/cache/epub/16389/pg16389.txt",
"https://www.gutenberg.org/cache/epub/5200/pg5200.txt",
"https://www.gutenberg.org/cache/epub/67979/pg67979.txt",
"https://www.gutenberg.org/cache/epub/394/pg394.txt",
"https://www.gutenberg.org/cache/epub/174/pg174.txt",
"https://www.gutenberg.org/cache/epub/6761/pg6761.txt",
"https://www.gutenberg.org/cache/epub/2160/pg2160.txt",
"https://www.gutenberg.org/cache/epub/98/pg98.txt",
"https://www.gutenberg.org/cache/epub/6593/pg6593.txt",
"https://www.gutenberg.org/cache/epub/4085/pg4085.txt",
"https://www.gutenberg.org/cache/epub/1259/pg1259.txt",
"https://www.gutenberg.org/cache/epub/5197/pg5197.txt",
"https://www.gutenberg.org/cache/epub/73442/pg73442.txt",
"https://www.gutenberg.org/cache/epub/1952/pg1952.txt",
"https://www.gutenberg.org/cache/epub/10681/pg10681.txt",
"https://www.gutenberg.org/cache/epub/2554/pg2554.txt",
"https://www.gutenberg.org/cache/epub/47629/pg47629.txt",
"https://www.gutenberg.org/cache/epub/345/pg345.txt",
"https://www.gutenberg.org/cache/epub/1080/pg1080.txt",
"https://www.gutenberg.org/cache/epub/52862/pg52862.txt",
"https://www.gutenberg.org/cache/epub/20228/pg20228.txt",
"https://www.gutenberg.org/cache/epub/25344/pg25344.txt",
"https://www.gutenberg.org/cache/epub/43/pg43.txt",
"https://www.gutenberg.org/cache/epub/73441/pg73441.txt",
"https://www.gutenberg.org/cache/epub/21700/pg21700.txt",
"https://www.gutenberg.org/cache/epub/1400/pg1400.txt",
"https://www.gutenberg.org/cache/epub/219/pg219.txt",
"https://www.gutenberg.org/cache/epub/10676/pg10676.txt",
"https://www.gutenberg.org/cache/epub/19694/pg19694.txt",
"https://www.gutenberg.org/cache/epub/62091/pg62091.txt",
"https://www.gutenberg.org/cache/epub/408/pg408.txt",
"https://www.gutenberg.org/cache/epub/28556/pg28556.txt",
"https://www.gutenberg.org/cache/epub/1260/pg1260.txt",
"https://www.gutenberg.org/cache/epub/38141/pg38141.txt",
"https://www.gutenberg.org/cache/epub/28054/pg28054.txt",
"https://www.gutenberg.org/cache/epub/76/pg76.txt",
"https://www.gutenberg.org/cache/epub/40438/pg40438.txt",
"https://www.gutenberg.org/cache/epub/2591/pg2591.txt",
"https://www.gutenberg.org/cache/epub/46/pg46.txt",
"https://www.gutenberg.org/cache/epub/1727/pg1727.txt",
"https://www.gutenberg.org/cache/epub/1661/pg1661.txt",
"https://www.gutenberg.org/cache/epub/42059/pg42059.txt",
"https://www.gutenberg.org/cache/epub/4300/pg4300.txt",
"https://www.gutenberg.org/cache/epub/2814/pg2814.txt",
"https://www.gutenberg.org/cache/epub/2000/pg2000.txt",
"https://www.gutenberg.org/cache/epub/1232/pg1232.txt",
"https://www.gutenberg.org/cache/epub/47475/pg47475.txt",
"https://www.gutenberg.org/cache/epub/6130/pg6130.txt",
"https://www.gutenberg.org/cache/epub/1998/pg1998.txt",
"https://www.gutenberg.org/cache/epub/768/pg768.txt",
"https://www.gutenberg.org/cache/epub/29870/pg29870.txt",
"https://www.gutenberg.org/cache/epub/996/pg996.txt",
"https://www.gutenberg.org/cache/epub/35899/pg35899.txt",
"https://www.gutenberg.org/cache/epub/2600/pg2600.txt",
"https://www.gutenberg.org/cache/epub/5740/pg5740.txt",
"https://www.gutenberg.org/cache/epub/39407/pg39407.txt",
"https://www.gutenberg.org/cache/epub/73447/pg73447.txt",
"https://www.gutenberg.org/cache/epub/120/pg120.txt",
"https://www.gutenberg.org/cache/epub/62354/pg62354.txt",
"https://www.gutenberg.org/cache/epub/54023/pg54023.txt",
"https://www.gutenberg.org/cache/epub/1184/pg1184.txt",
"https://www.gutenberg.org/cache/epub/67098/pg67098.txt",
"https://www.gutenberg.org/cache/epub/45/pg45.txt",
"https://www.gutenberg.org/cache/epub/3207/pg3207.txt",
"https://www.gutenberg.org/cache/epub/2852/pg2852.txt",
"https://www.gutenberg.org/cache/epub/5131/pg5131.txt",
"https://www.gutenberg.org/cache/epub/27827/pg27827.txt",
"https://www.gutenberg.org/cache/epub/55/pg55.txt",
"https://www.gutenberg.org/cache/epub/16/pg16.txt",
"https://www.gutenberg.org/cache/epub/74/pg74.txt",
"https://www.gutenberg.org/cache/epub/244/pg244.txt",
"https://www.gutenberg.org/cache/epub/24238/pg24238.txt",
"https://www.gutenberg.org/cache/epub/600/pg600.txt",
"https://www.gutenberg.org/cache/epub/30254/pg30254.txt",
"https://www.gutenberg.org/cache/epub/205/pg205.txt",
"https://www.gutenberg.org/cache/epub/23/pg23.txt",
"https://www.gutenberg.org/cache/epub/514/pg514.txt",
"https://www.gutenberg.org/cache/epub/7370/pg7370.txt",
"https://www.gutenberg.org/cache/epub/4363/pg4363.txt",
"https://www.gutenberg.org/cache/epub/33283/pg33283.txt",
"https://www.gutenberg.org/cache/epub/19926/pg19926.txt",
"https://www.gutenberg.org/cache/epub/73444/pg73444.txt",
"https://www.gutenberg.org/cache/epub/3825/pg3825.txt",
"https://www.gutenberg.org/cache/epub/41445/pg41445.txt",
"https://www.gutenberg.org/cache/epub/8800/pg8800.txt"
]

# Lista para almacenar enlaces inexistentes
enlaces_inexistentes = []

# Carpeta donde se guardarán los archivos txt descargados
carpeta_destino = "data"

# Crear la carpeta si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Iterar sobre cada enlace
for enlace in enlaces:
    # Obtener el nombre del archivo desde el enlace
    nombre_archivo = enlace.split("/")[-1]
    # Ruta completa del archivo en el sistema local
    ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)

    # Realizar la petición GET al enlace
    response = requests.get(enlace)

    # Verificar si la respuesta es exitosa (código de estado 200)
    if response.status_code == 200:
        # Guardar el contenido en un archivo txt
        with open(ruta_archivo, "wb") as archivo:
            archivo.write(response.content)
        print(f"Archivo descargado: {nombre_archivo}")
    else:
        # Almacenar enlace inexistente en la lista correspondiente
        enlaces_inexistentes.append(enlace)

# Imprimir enlaces inexistentes
if enlaces_inexistentes:
    print("\nEnlaces inexistentes:")
    for enlace_inexistente in enlaces_inexistentes:
        print(enlace_inexistente)
else:
    print("\nTodos los enlaces fueron descargados exitosamente.")
