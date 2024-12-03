"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    with open("files/input/data.csv") as file:
        lines = file.readlines()
        data= []
        for line in lines:
            fila = (line.replace("\t", " ").strip().split()[0], line.replace("\t", " ").strip().split()[1])
            data.append(fila)
        diccionario = {}
        for letra, numero in data:
            if numero not in diccionario:
                diccionario[numero] = [letra]
            else:
                if letra not in diccionario[numero]:
                    diccionario[numero].append(letra)
        diccionario = dict(sorted(diccionario.items()))
        for clave in diccionario:
            diccionario[clave] = sorted(diccionario[clave])
        resultado = [(int(clave), diccionario[clave]) for clave in diccionario]
        return resultado