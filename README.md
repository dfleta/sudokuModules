# sudokuModules

Kata sobre programación modular en Python.

Se trata de investigar y comprender los contextos de ejecución al invocar módulos Python.

Por este motivo, la configuración del `sys.path` en el código de `checkSudoku.py` y los `import`
de las dependencias se han hecho explícitas. Lee los comentarios en el código.

Además, se incluyen unos prints estilo _devil guide to debugging_ en `checkCuadrado.py`para hacer explícita la ejecución del código de un módulo cuando lo importamos y entender el comportamiento de los _Mixed Usage Modes_ `__name__` y ` __main__`.

La estructura de directorios y sus nombres tampoco son muy ortodoxas ya que responden a la intención de forzar comportamientos para comprender el sistema de importación de módulos de Python.

No se utiliza una suite de testing, ya que se accede a los casos test utilizando la **reflexión** de Python, accediendo a los mismos como propiedades del objeto módulo `casosTestSudoku.py`.

No se utiliza el nombre `test` en el directorio con los casos test porque sino el entorno Python intenta importar desde ese paquete los módulos que no encuentra cuando importamos el contenido del directorio con los casos test (precedencia de nombre).

## Cómo ejecutarlo

Ejecutar `sudoku.py` desde consola en el directorio raíz del proyecto IS OK.

`$ python3 sudoku.py`

Ejecutar `checkSudoku.py` desde el directorio raíz del proyecto IS NOT OK pues el contexto de
ejecución será el directorio raíz y al cambiar el `path` a `..` las rutas relativas a las depedencias no se construyen bien.

`$ python3 src/checkSudoku.py` NO!!

Ejecutar `checkSudoku.py` desde el directorio `src` del proyecto IS OK:

`src $ python3 checkSudoku.py`

Ejecutar cada módulo de las funciones SRP desde el contexto `src` IS OK:

`src $ python3 checkCuadrado.py`
