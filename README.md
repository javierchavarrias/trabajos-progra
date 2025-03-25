<<<<<<< HEAD
# trabajos-progra
# Calculadora de Polinomios

Este proyecto implementa una calculadora de polinomios en Python que permite realizar operaciones básicas como suma, resta, multiplicación, división y evaluación de polinomios representados mediante diccionarios.

## Qué hace esta calculadora

- Permite introducir polinomios manualmente o desde un fichero.
- Soporta dos modos de carga:
  - Modo manual / archivo único: introduce un polinomio por línea.
  - Modo fichero completo: un fichero con formato estructurado que ejecuta automáticamente la operación.
- Permite calcular:
  - Suma
  - Resta
  - Multiplicación
  - División (incluye el resto)
  - Evaluación para un valor x
  - 
## Estructura del proyecto

- calculadora.py  : Interfaz de consola (menú de opciones)
- polinomios.py : Clase Polinomio con todas las operaciones
- ficheros.py : Funciones para leer y guardar ficheros

## Formatos de entrada

### Ejemplo de entrada manual:

4x^2 -6x +3

Debes tener en cuenta que entre los diferentes términos debes dejar un espacio y el signo ponérselo a los coeficientes
### Ejemplo de fichero completo (miarchivo.txt):


- POLINOMIO 1: 2x^2 - 4 
- POLINOMIO 2: x^2 + 1 
- OPERACIÓN: MULTIPLICACION


### Ejemplo de fichero de evaluación:

- POLINOMIO 1: 2x^2 - 4
- NUMERO: 2
- OPERACIÓN: EVALUACIÓN
