def leer_polinomios_desde_fichero(nombre_fichero):
    """Lee un fichero con polinomios y devuelve los datos en un diccionario."""
    polinomios = {}
    try:
        with open(nombre_fichero, 'r') as f:
            lineas = f.readlines()

        for linea in lineas:
            if linea.startswith("POLINOMIO 1:"):
                polinomios['p1'] = linea.split(":")[-1].strip()
            elif linea.startswith("POLINOMIO 2:"):
                polinomios['p2'] = linea.split(":")[-1].strip()
            elif linea.startswith("NUMERO:"):
                polinomios['numero'] = float(linea.split(":")[-1].strip())
            elif linea.startswith("OPERACIÓN:"):
                polinomios['operacion'] = linea.split(":")[-1].strip().upper()

        return polinomios
    except FileNotFoundError:
        print("Error: Fichero no encontrado.")
        return None


def guardar_resultado_en_fichero(nombre_fichero, resultado):
    """Guarda el resultado de la operación en un fichero usando writelines."""
    with open(nombre_fichero, 'w') as f:
        if isinstance(resultado, dict):
            for clave, valor_en_resultado.items():
                f.writelines(f"{clave}: {valor}\n")
        else:
            f.write(str(resultado))
    print(f"Resultado guardado en {nombre_fichero}")