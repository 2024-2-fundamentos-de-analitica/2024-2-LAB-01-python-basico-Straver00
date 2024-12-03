"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv") as file:
        lines = file.readlines()
        data= []
        for line in lines:
            fila = line.replace("\t", ",").strip().split(",")
            data.append(fila)
        letras = []
        for i in range(len(data)):
            letras.append((data[i][0], data[i][1]))
        letras_unicas = list(set(letras))
        diccionario = {}
        for letra, valor in letras:
            valor = int(valor)
            if letra not in diccionario:
                diccionario[letra] = {"min":valor, "max":valor}
            else:
                if valor < diccionario[letra]["min"]:
                    diccionario[letra]["min"] = valor
                if valor > diccionario[letra]["max"]:
                    diccionario[letra]["max"] = valor
        diccionario = dict(sorted(diccionario.items()))
        resultado = [(clave, diccionario[clave]["max"], diccionario[clave]["min"]) for clave in diccionario]
        return resultado
        

print(pregunta_05())