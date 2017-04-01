""" Esta clase sirve para generar el grafo que tomara el algoritmo hungaro """
import json as js
from copy import deepcopy

class Graph(object):
    """ Se construye la matriz de pesos a partir de un objeto json """

    asignaciones = [[]]
    matriz_original = [[]]

    def __init__(self, json):
        self._obj = js.loads(json)
        self.len = len(self._obj)

    def construir_matriz(self):
        """ Aca creamos la matriz de pesos y le restamos los mínimos a cada fila """
        matrix = 0
        var_x = var_y = self.len
        var_w = var_s = 0

        if var_x != 0:
            self.asignaciones = [[0 for i in range(var_x)] for j in range(var_y)]
            matrix = [[0 for i in range(var_x)] for j in range(var_y)]
            for var_va in self._obj:
                for var_vb in self._obj[var_va]:
                    self.asignaciones[var_w][var_s] = (str(var_va), str(var_vb))
                    matrix[var_w][var_s] = int(self._obj[var_va][var_vb])
                    var_s = var_s + 1
                var_w = var_w + 1
                var_s = 0

            self.matriz_original = deepcopy(matrix)
            var_min = minimo_fila(matrix)
            restar_minimos(matrix, var_min)

        return matrix

    def elementos_del_matching(self):
        """ devuelve los vertices del grafo, o sea los que se asignan """
        return self.asignaciones

    def matriz_pesos(self):
        """ Devuelve la matríz con los pesos originales """
        return self.matriz_original

    def pesos_print(self):
        """ Imprime la matriz con los pesos originales"""
        var_n = self.len
        for i in range(var_n):
            print(self.matriz_original[i])

    def asignaciones_print(self):
        """ Imprime la matriz de asignados """
        print(self.asignaciones)


# Funciones auxiliares
def minimo_fila(matrix):
    """ Calculamos el minimo de cada fila y lo guardamos en un array """
    var_n = len(matrix)
    var_min = [0 for i in range(var_n)]
    i = 0
    while i < var_n:
        var_min[i] = min(matrix[i]) # Mínimo de cada fila
        i = i + 1
    return var_min

def restar_minimos(matrix, var_min):
    """ Restamos el minimo a cada fila """
    var_n = len(matrix)
    for i in range(var_n):
        for j in range(var_n):
            matrix[i][j] = matrix[i][j] - var_min[i]
    return matrix