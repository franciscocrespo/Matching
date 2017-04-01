""" Esta clase sirve para generar el grafo que tomara el algoritmo hungaro """
import json as js

class Graph(object):
    """ Se construye la matriz de pesos a partir de un objeto json """

    _asignaciones = [[]]

    def __init__(self, json):
        self._obj = js.loads(json)
        self.len = len(self._obj)

    def build(self):
        matrix = 0
        x = y = self.len
        w = s = 0

        if x != 0:
            self._asignaciones = [[0 for i in range(x)] for j in range(y)]
            matrix = [[0 for i in range(x)] for j in range(y)]
            for ka, va in self._obj.iteritems():
                for kb, vb in va.iteritems():
                    self._asignaciones[w][s] = (str(ka), str(kb))
                    matrix[w][s] = int(vb)
                    s = s + 1
                w = w + 1
                s = 0

                min = minimo_fila(matrix)
                restar_minimos(matrix, min)

        return matrix

    def pesos_print(self, matrix):
        """ Imprime la matriz """
        print matrix

    def asignaciones_print(self):
        """ Imprime la matriz de asignados """
        print self._asignaciones


def minimo_fila(matrix):
    """ Calculamos el minimo de cada fila y lo guardamos en un array """
    n = len(matrix)
    min = [0 for i in range(n)]
    i = j = val = 0
    while i < n:
        while j < n - 1:
            val = matrix[i][j]
            if val > matrix[i][j+1]:
                val = matrix[i][j+1]
            min[i] = val
            j = j + 1
        i = i + 1
        j = 0
    return min

def restar_minimos(matrix, min):
    """ Restamos el minimo a cada fila """
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix[i][j] - min[i]
    return matrix