correcto = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

numero_repetido_fila_columna = [[1, 2, 3, 4],
                                [2, 3, 1, 3],
                                [3, 1, 2, 3],
                                [4, 4, 4, 2]]

numero_repetido_columna =   [[1, 2, 3],
                            [2, 3, 1],
                            [2, 3, 1]]

numero_no_presente =    [[1, 2, 3, 4],
                        [2, 3, 1, 2],
                        [4, 1, 2, 3],
                        [2, 3, 1, 4]]

numero_fuera_del_rango =    [[1, 2, 3, 4, 5],
                            [2, 3, 1, 5, 6],
                            [4, 5, 2, 1, 3],
                            [3, 4, 5, 2, 1],
                            [5, 6, 4, 3, 2]]

caracteres = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

numeros_reales =    [[1, 1.5],
                    [1.5, 1]]

irregular_fila =    [[1, 2, 3],
                    [2, 3, 1]]

irregular_columna = [[1, 2, 3],
                    [2, 3, 1],
                    [3, 1]]

lista_vacia = [[]]

# Para evitar importar una variable al usar:
# from modulo import *
# se emplea __nombreVariable
# En nuestro caso utilizo import as
# porque necesito noombrar el espacio de nombres
# que define de este modulo
# por lo que no puedo usar *
# Este caso test no pasa el filtro
# attr.startswith('__') el el main

__oculto = [[1]]
