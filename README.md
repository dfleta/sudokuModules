# sudokuModules

Kata sobre programación modular en Python.

Se trata de investigar y comprender los contextos de ejecución al invocar módulos Python.

Por este motivo, la configuración del `sys.path` en el código de `checkSudoku.py` y los `import`
de las dependencias se han hecho explícitas. Lee los comentarios en el código.

Además, se incluyen unos prints estilo _devil guide to debugging_ en `checkCuadrado.py`para hacer explícita la ejecución del código de un módulo cuando lo importamos y entender el comportamiento
de los _Mixed Usage Modes_ `__name__` y ` __main__`.

Ejecutar `sudoku.py` desde consola en el directorio raíz del proyecto IS OK.

`$ python3 sudoku.py`

Ejecutar `checkSudoku.py` desde el directorio raíz del proyecto IS NOT OK pues el contexto de
ejecución será el directorio raíz y al cambiar el `path` a `..` las rutas relativas a las depedencias no se construyen bien.

`$ python3 src/checkSudoku.py` NO!!

Ejecutar `checkSudoku.py` desde el directorio `src` del proyecto IS OK:

`src $ python3 checkSudoku.py`

Ejecutar cada módulo de las funciones SRP desde el contexto `src` IS OK:

`src $ python3 checkCuadrado.py`
