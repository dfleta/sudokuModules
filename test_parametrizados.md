# Documentación de Pruebas con Pytest

Este documento explica la configuración de los markers y el uso de casos de prueba parametrizados en el proyecto de Sudoku. Estas herramientas son fundamentales para organizar y estructurar las pruebas de manera eficiente.

---

## Configuración de Markers

En el archivo `pytest.ini`, se han definido los siguientes markers para categorizar las pruebas:

### 1. **barricada**
- **Descripción**: Marca situaciones que implican precondiciones necesarias para ejecutar las pruebas.
- **Uso**: Se utiliza para validar que las condiciones iniciales del Sudoku son correctas antes de realizar otras pruebas.
- **Ejemplo**:
    ```python
    @pytest.mark.barricada
    def test_precondiciones():
        # Código para validar precondiciones
        assert True
    ```

### 2. **es_cuadrado**
- **Descripción**: Verifica que el Sudoku es una matriz cuadrada de tamaño `n x n`.
- **Uso**: Asegura que la estructura del Sudoku cumple con los requisitos básicos.
- **Ejemplo**:
    ```python
    @pytest.mark.es_cuadrado
    def test_es_cuadrado():
        sudoku = [[1, 2], [3, 4]]
        assert checkCuadrado(sudoku) == True
    ```

### 3. **numeros_validos**
- **Descripción**: Comprueba que el Sudoku está formado por números enteros en el rango permitido (1 a `n`).
- **Uso**: Garantiza que los valores en la matriz son válidos.
- **Ejemplo**:
    ```python
    @pytest.mark.numeros_validos
    def test_numeros_validos():
        sudoku = [[1, 2], [3, 4]]
        assert all(1 <= num <= 4 for row in sudoku for num in row)
    ```

### 4. **filas_validas**
- **Descripción**: Verifica que no existen números repetidos en las filas del Sudoku.
- **Uso**: Asegura que cada fila contiene valores únicos.
- **Ejemplo**:
    ```python
    @pytest.mark.filas_validas
    def test_filas_validas():
        sudoku = [[1, 2], [3, 4]]
        assert all(len(set(row)) == len(row) for row in sudoku)
    ```

### 5. **columnas_validas**
- **Descripción**: Verifica que no existen números repetidos en las columnas del Sudoku.
- **Uso**: Asegura que cada columna contiene valores únicos.
- **Ejemplo**:
    ```python
    @pytest.mark.columnas_validas
    def test_columnas_validas():
        sudoku = [[1, 2], [3, 4]]
        transposed = zip(*sudoku)
        assert all(len(set(col)) == len(col) for col in transposed)
    ```

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