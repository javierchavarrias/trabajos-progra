def leer_fichero(nombre_fichero):
    """Lee un fichero que contiene un único polinomio en una línea."""
    try:
        with open(nombre_fichero, 'r') as f:
            linea = f.readline().strip()
        return linea
    except FileNotFoundError:
        print("Error: Fichero no encontrado.")
        return None