import polinomios
import ficheros

def menu_opciones():
    """Muestra el menú de opciones y ejecuta la operación elegida."""
    print("\033[1m¡Bienvenido a la calculadora de polinomios!\033[0m")
    print("-------------------")
    resultado = None

    while True:
        if resultado is None:
            print("Vamos a introducir el \033[1mPolinomio 1.\033[0m")
            print("")
            print(
                "Si desea introducirlo manualmente, hágalo directamente siguiendo esta estructura (\033[3m4x^2 -6x +3\033[0m)")
            print("o si desaa cargarlo desde un archivo, escriba F ")
            print("")
            modo_entrada = input("").strip().lower()
            if modo_entrada == 'f':
                archivo = input("Introduzca el nombre del archivo: ")
                polinomio1 = leer_fichero(archivo)
            else:
                polinomio1 = cargar_polinomio_desde_texto(modo_entrada)
        else:
            polinomio1 = resultado
            print("Usando el resultado anterior como polinomio 1.")

    print("")
    print("--------")
    print("")
    print("\033[1mSeleccione la operación que desea realizar\033[0m")
    print("")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Evaluación")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")


menu_opciones()

