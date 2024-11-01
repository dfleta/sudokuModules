Sudoku Modules
==============

Kata sobre programación modular en Python, a partir de uno de los ejercicios propuestos en el _problem set_ de la _Lesson 3: How to Manage Data_ del curso [_Intro to computer science_](https://www.youtube.com/watch?v=9nkR2LLPiYo&list=PLAwxTw4SYaPmjFQ2w9j05WDX8Jtg5RXWW) del Prof. Dave Evans [@evansuva](https://github.com/evansuva) en Udacity. 

Se trata de investigar y comprender los contextos de ejecución al invocar módulos Python.

Por este motivo, la configuración del `sys.path` en el código de `checkSudoku.py` y los `import`
de las dependencias se han hecho explícitas. Lee los comentarios en el código.

Además, se incluyen unos prints estilo _devil guide to debugging_ en `checkCuadrado.py`para hacer explícita la ejecución del código de un módulo cuando lo importamos y entender el comportamiento de los _Mixed Usage Modes_ `__name__` y ` __main__`.

La estructura de directorios y sus nombres tampoco son muy ortodoxas ya que responden a la intención de forzar comportamientos para comprender el sistema de importación de módulos de Python.

No se utiliza una suite de testing, ya que se accede a los casos test utilizando la **reflexión** de Python, accediendo a los mismos como propiedades del objeto módulo `casosTestSudoku.py`.

No se utiliza el nombre `test` en el directorio con los casos test porque sino el entorno Python intenta importar desde ese paquete los módulos que no encuentra cuando importamos el contenido del directorio con los casos test (precedencia de nombre).

## Uso

Ejecutar `sudoku.py` desde consola en el directorio raíz del proyecto IS OK:

`$ python3 sudoku.py`

Ejecutar `checkSudoku.py` desde el directorio raíz del proyecto IS NOT OK 
pues el contexto de ejecución será el directorio raíz y al cambiar el `path` a `..` las rutas relativas a las depedencias no se construyen bien.

`$ python3 src/checkSudoku.py` IS NOT OK

Ejecutar `checkSudoku.py` desde el directorio `src` del proyecto IS OK:

`src $ python3 checkSudoku.py`

Ejecutar cada módulo de las funciones SRP desde el contexto `src` IS OK:

`src $ python3 checkCuadrado.py`

## Casos test

Cómo parametrizar casos test:

- [How to parametrize fixtures and test functions](https://docs.pytest.org/en/stable/how-to/parametrize.html)

- [Parametrization examples.](https://docs.pytest.org/en/stable/example/parametrize.html#paramexamples)

### Uso

```python
[pytest]
markers = 
    barricada: situaciones que implican precondiciones
    es_cuadrado: el sudoku es una matriz n*n
    numeros_validos: el sudoku esta formado por numeros enteros en el rango 1 a numeros
    filas_validas: no existen numeros repetidos en las filas
    columnas_validas: no existen numeros repetidos en las columnas
```

En los casos test parametrizados utilizamos el marker con esta notación:

```python
@pytest.mark.filas_validas
@pytest.mark.parametrize("sudoku, sano",
                         # resto de casos test
                         [pytest.param(casosTest.numero_fuera_del_rango,
                                         True,
                                         marks=pytest.mark.barricada)])
```

Selección del marker de los casos test parametrizados:

`pytest -m barricada`

Selección del marker en el resto de casos test:

`pytest -m numeros_validos`
