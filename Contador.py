import matplotlib.pyplot as plt
from collections import Counter
import re

# Función para limpiar y contar palabras
def contar_palabras(archivo_txt):
    with open(archivo_txt, 'r', encoding='utf-8') as archivo:
        texto = archivo.read().lower()  # Lee el archivo y convierte a minúsculas

    # Eliminar puntuación y caracteres especiales, quedándonos solo con palabras
    palabras = re.findall(r'\b\w+\b', texto)

    # Contar la frecuencia de cada palabra
    contador = Counter(palabras)

    # Obtener las 3 palabras más frecuentes
    palabras_comunes = contador.most_common(3)

    return palabras_comunes

# Función para graficar
def graficar_frecuencia(palabras_frecuencia):
    palabras, frecuencias = zip(*palabras_frecuencia)
    
    # Crear el gráfico de barras
    plt.bar(palabras, frecuencias, color='skyblue')
    plt.xlabel('Palabras')
    plt.ylabel('Repeticiones')
    plt.title('Top 3 Palabras Más Frecuentes')
    plt.xticks(rotation=40)  # Rotar etiquetas para que se vean mejor
    plt.tight_layout()  # Ajustar el layout para que las etiquetas no se corten
    plt.show()

# Ruta del archivo .txt
archivo_txt = 'Entrada.txt'

# Contar palabras y graficar resultados
palabras_frecuencia = contar_palabras(archivo_txt)
graficar_frecuencia(palabras_frecuencia)
