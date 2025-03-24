def leer_fichero(nombre_fichero):
    """Lee un fichero que contiene un único polinomio en una línea."""
    datos={}
    try:
        with open(nombre_fichero, 'r') as f:
            lineas = f.readlines()

        for linea in lineas:
            linea = linea.strip()
            if linea.startswith("POLINOMIO 1:"):
                datos['p1'] = linea.split(":")[-1].strip()
            elif linea.startswith("POLINOMIO 2:"):
                datos['p2'] = linea.split(":")[-1].strip()
            elif linea.startswith("NUMERO:"):
                datos['numero'] = float(linea.split(":")[-1].strip())
            elif linea.startswith("OPERACIÓN:"):
                datos['operacion'] = linea.split(":")[-1].strip().upper()

        if 'operacion' not in datos:
            with open(nombre_fichero, 'r') as f:
                linea = f.readline().strip()
         return linea
    except FileNotFoundError:
        print("Error: Fichero no encontrado.")
        return None

def descargar_fichero(nombre_fichero, resultado):
    """Guarda el resultado de la operación en un fichero de texto."""
    with open(nombre_fichero, 'w') as f:
        f.write(str(resultado))
    print(f"Resultado guardado en {nombre_fichero}")
