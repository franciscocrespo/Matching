""" Esta clase sirve para generar el grafo que tomara el algoritmo hungaro """
import json as js

class Graph(object):
    """ Se construye la matriz de pesos a partir de un objeto json """

    _asignaciones = [[]]

    def __init__(self, json):
        self._obj = js.loads(json)
        self.len = len(self._obj)

    def build_matrix(self):
        """ Aca creamos la matriz de pesos y le restamos los mínimos a cada fila """
        matrix = 0
        var_x = var_y = self.len
        var_w = var_s = 0

        if var_x != 0:
            self._asignaciones = [[0 for i in range(var_x)] for j in range(var_y)]
            matrix = [[0 for i in range(var_x)] for j in range(var_y)]
            for var_va in self._obj:
                for var_vb in self._obj[var_va]:
                    print(self._obj[var_va][var_vb])
                    self._asignaciones[var_w][var_s] = (str(var_va), str(var_vb))
                    matrix[var_w][var_s] = int(self._obj[var_va][var_vb])
                    var_s = var_s + 1
                var_w = var_w + 1
                var_s = 0

                var_min = minimo_fila(matrix)
                restar_minimos(matrix, var_min)

        return matrix

    def pesos_print(self, matrix):
        """ Imprime la matriz """
        print(matrix)

    def asignaciones_print(self):
        """ Imprime la matriz de asignados """
        print(self._asignaciones)


# Funciones auxiliares
def minimo_fila(matrix):
    """ Calculamos el minimo de cada fila y lo guardamos en un array """
    var_n = len(matrix)
    var_min = [0 for i in range(var_n)]
    i = j = val = 0
    while i < var_n:
        while j < var_n - 1:
            val = matrix[i][j]
            if val > matrix[i][j+1]:
                val = matrix[i][j+1]
            var_min[i] = val
            j = j + 1
        i = i + 1
        j = 0
    return var_min

def restar_minimos(matrix, min):
    """ Restamos el minimo a cada fila """
    var_n = len(matrix)
    for i in range(var_n):
        for j in range(var_n):
            matrix[i][j] = matrix[i][j] - min[i]
    return matrix