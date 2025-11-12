# Documentación de Pruebas con Pytest

[Texto generado con Claude a partir de mi código]

Este documento explica la configuración de los markers y el uso de casos de prueba parametrizados en el proyecto de Sudoku. 

Estas herramientas son fundamentales para organizar y estructurar las pruebas de manera eficiente.

---

## Configuración de Markers

En el archivo `pytest.ini`, se han definido los siguientes _markers_ para categorizar las pruebas:

```
[pytest]
markers = 
    barricada: situaciones que implican precondiciones
    es_cuadrado: el sudoku es una matriz n*n
    numeros_validos: el sudoku esta formado por numeros enteros en el rango 1 a numeros
    filas_validas: no existen numeros repetidos en las filas
    columnas_validas: no existen numeros repetidos en las columnas
```

### 1. **barricada**
- **Descripción**: Marca situaciones que implican precondiciones necesarias para ejecutar las pruebas.
- **Uso**: Se utiliza para validar que las condiciones iniciales del Sudoku son correctas antes de realizar otras pruebas.
- **Ejemplo**:
    ```python
    @pytest.mark.parametrize("sudoku, sano",
                            [ pytest.param(casosTest.numero_fuera_del_rango,
                                            False,
                                            marks=pytest.mark.barricada),
                            ])
    def test_check_sudoku(sudoku, sano):
        assert checkSudoku(sudoku) == sano
    ```

### 2. **es_cuadrado**
- **Descripción**: Verifica que el Sudoku es una matriz cuadrada de tamaño `n x n`.
- **Uso**: Asegura que la estructura del Sudoku cumple con los requisitos básicos.
- **Ejemplo**:
    ```python
    @pytest.mark.es_cuadrado
    def test_es_cuadrado():
        sudoku = [[1, 2], [3, 4]]
        assert checkCuadrado(sudoku) is True
    ```

### 3. **numeros_validos**
- **Descripción**: Comprueba que el Sudoku está formado por números enteros en el rango permitido (1 a `n`).
- **Uso**: Garantiza que los valores en la matriz son válidos.
- **Ejemplo**:
    ```python
    @pytest.mark.numeros_validos
    def test_numeros_validos():
        sudoku = [[1, 2], [3, 4]]
        assert checkNumerosValidos(sudoku)
    ```

### 4. **filas_validas**
- **Descripción**: Verifica que no existen números repetidos en las filas del Sudoku.
- **Uso**: Asegura que cada fila contiene valores únicos.
- **Ejemplo**:
    ```python
    @pytest.mark.filas_validas
    def test_filas_validas():
        sudoku = [[1, 2], [3, 4]]
        assert checkFilas(sudoku)
    ```

### 5. **columnas_validas**
- **Descripción**: Verifica que no existen números repetidos en las columnas del Sudoku.
- **Uso**: Asegura que cada columna contiene valores únicos.
- **Ejemplo**:
    ```python
    @pytest.mark.columnas_validas
    def test_columnas_validas():
        sudoku = [[1, 2], [3, 4]]
        assert checkcolumnas(sudoku)
    ```

### ¿Para qué sirve marks=pytest.mark.barricada?

Las marcas permiten:

1. Ejecutar selectivamente tests

```python
# Ejecutar SOLO los tests marcados con 'barricada'
pytest -m barricada

# Ejecutar todos EXCEPTO los marcados con 'barricada'
pytest -m "not barricada"
```

2. Agrupar casos de prueba relacionados
En este caso, barricada indica un test de barrera o test defensivo que verifica que el código rechaza entrada inválida (números fuera de rango).

3. Documentación y organización

Las marcas sirven como etiquetas para categorizar tests:

- Tests de validación de entrada
- Tests de casos límite
- Tests de regresión
- Tests lentos

---

## Casos de Prueba Parametrizados

### ¿Qué son los casos de prueba parametrizados?
Los casos de prueba parametrizados permiten ejecutar una misma prueba con diferentes conjuntos de datos. Esto es útil para evitar la duplicación de código y garantizar que las pruebas cubran múltiples escenarios.

### Ejemplo de Caso Parametrizado
A continuación, se muestra un ejemplo de prueba parametrizada para verificar si una matriz es cuadrada:

```python
import pytest
from src.checkCuadrado import checkCuadrado

@pytest.mark.parametrize(
    "sudoku, esperado",
    [
        ([[1, 2], [3, 4]], True),  # Caso válido
        ([[1, 2, 3], [4, 5, 6]], False),  # Caso inválido
        ([[1]], True),  # Caso borde
    ]
)
def test_es_cuadrado_parametrizado(sudoku, esperado):
    assert checkCuadrado(sudoku) == esperado
```

### ¿Qué es @pytest.mark.parametrize?

Es un decorador de pytest que permite ejecutar la misma función de test múltiples veces con diferentes conjuntos de datos de entrada. 

Es una forma elegante de evitar duplicar código cuando quieres probar la misma funcionalidad con distintos casos.

Componentes:

1. Primer argumento: "sudoku, esperado"
    * Define los nombres de los parámetros que recibirá la función de test
    * Se pasan como una cadena separada por comas
    * Estos nombres deben coincidir con los parámetros de la función de test
2. Segundo argumento: lista de tuplas

```python
[
    ([[1, 2], [3, 4]], True),        # Caso válido
    ([[1, 2, 3], [4, 5, 6]], False), # Caso inválido
    ([[1]], True),                   # Caso válido
]
```

* Cada tupla representa un conjunto de valores de prueba
* Cada elemento de la tupla corresponde a un parámetro en orden:
    - Primer elemento → sudoku
    - Segundo elemento → esperado

#### ¿Cómo funciona?

Pytest genera automáticamente 3 tests (uno por cada tupla):

Test 1: `sudoku=[[1, 2], [3, 4]], esperado=True`

Test 2: `sudoku=[[1, 2, 3], [4, 5, 6]], esperado=False`

Test 3: `sudoku=[[1]], esperado=True`

Cada test se ejecuta de forma independiente y se reporta por separado en la salida de pytest.

Ventajas:

✅ Reduce duplicación: Una función de test en lugar de tres

✅ Legibilidad: Los casos de prueba están claramente definidos

✅ Mantenibilidad: Es fácil añadir más casos

✅ Reportes claros: Pytest indica qué caso específico falló

### ¿Qué es pytest.param?

Es una función de pytest que permite especificar parámetros individuales con configuración adicional, en lugar de usar solo tuplas simples.

```python
@pytest.mark.parametrize("sudoku, sano",
                         [  pytest.param(casosTest.numero_fuera_del_rango,
                                         False,
                                         marks=pytest.mark.barricada),
                         ])
def test_check_sudoku(sudoku, sano):
    assert checkSudoku(sudoku) == sano
```


Componentes:

1. Primer argumento: `casosTest.numero_fuera_del_rango`
    * Valor para el parámetro `sudoku`
    * Un caso de prueba donde los números están fuera del rango válido

2. Segundo argumento: `False`
    * Valor para el parámetro `sano`
    * El resultado esperado: el sudoku NO es válido

3. `marks=pytest.mark.barricada`
    * Añade una marca personalizada a este caso de prueba específico
    * La marca se llama `barricada`, aunque elegir el nombre que prefieras

#### ¿Por qué usar esto en lugar de una tupla simple?

Ventaja principal: Puedes ejecutar o excluir este caso específico sin necesidad de crear una función de test separada.

Por ejemplo, si los tests de barricada son lentos o requieren configuración especial


### Resumen:

- `pytest.param` es una versión avanzada de las tuplas en parametrize
- `marks=` añade etiquetas/marcas a casos de prueba individuales
- `pytest.mark.barricada` marca personalizada para identificar este tipo de test
- Permite ejecución selectiva de subconjuntos de casos parametrizados
