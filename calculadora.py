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
            print("Si desea introducirlo manualmente, hágalo directamente siguiendo esta estructura (\033[3m4x^2 -6x +3\033[0m)")
            print("o si desaa cargar el polinomio 1 desde un archivo, escriba A ")
            print("Sin embargo, si desea usar el modo fichero completo escriba F")
            print("")
            modo_entrada = input("").strip().lower()
            if modo_entrada == 'f':
                archivo = input("Introduzca el nombre del archivo: ")
                polinomio1 = ficheros.leer_fichero_completo(archivo)
            elif modo_entrada == 'a':
                archivo = input("Introduzca el nombre del archivo: ")
                polinomio1 = ficheros.leer_fichero_unico(archivo)
            else:
                polinomio1 = polinomios.cargar_polinomio_desde_texto(modo_entrada)
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
        if opcion == '6':
            print("Saliendo del programa.")
            break
        if opcion in ['1', '2', '3', '4']:
            print("")
            print("--------")
            print("Vamos a introducir el \033[1mPolinomio 2.\033[0m")
            print("")
            print(
                "Para introducir el Polinonio 2 puede hacerlo manualmente, escribiéndolo directamente siguiendo esta estructura (\033[3m4x^2 -6x +3\033[0m)")
            print("o si desaa cargarlo desde un archivo, escriba F ")
            modo_entrada2 = input("").strip().lower()

            if modo_entrada2 == 'f':
                archivo2 = input("Introduzca el nombre del archivo: ")
                polinomio2 = ficheros.leer_fichero(archivo2)
            else:
                polinomio2 = polinomios.cargar_polinomio_desde_texto(modo_entrada2)
            if opcion == '1':
                resultado = polinomio1.suma(polinomio2)
            elif opcion == '2':
                resultado = polinomio1.resta(polinomio2)
            elif opcion == '3':
                resultado = polinomio1.multiplicacion(polinomio2)
            elif opcion == '4':
                resultado, resto = polinomio1.division(polinomio2)
        elif opcion == '5':
            x = float(input("Introduzca el valor de x: "))
            resultado = polinomio1.evaluar(x)
        else:
            print("Opción inválida.")
            continue
        print("")
        print("--------")
        print(f"\033[1mResultado: {resultado}\033[0m")
        if opcion == 4:
            print(f"Resto: {resto}")
        print("--------")
        print("")
        print("")
        print("\033[1m¿Qué desea hacer ahora?\033[0m")
        print("1. \033[1mSalir\033[0m de la calculadora")
        print("2. \033[1mDescargar\033[0m el resultado en un archivo")
        print("3. \033[1mSeguir\033[0m calculando con el \033[1mresultado como Polinomio 1\033[0m")
        print("4. \033[1mSeguir\033[0m calculando con un \033[1mnuevo Polinomio 1\033[0m")

        siguiente_opcion = input("Seleccione una opción: ")
        if siguiente_opcion == '1':
            print("Saliendo del programa.")
            break
        elif siguiente_opcion == '2':
            nombre_archivo = input("Introduzca el nombre del archivo para guardar el resultado: ")
            ficheros.descargar_fichero(nombre_archivo, resultado)
            print("Resultado guardado correctamente.")
        elif siguiente_opcion == '3':
            continue
        elif siguiente_opcion == '4':
            resultado = None
        else:
            print("Opción inválida. Volviendo al menú de operaciones.")


menu_opciones()

