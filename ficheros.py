def leer_fichero(nombre_fichero):
    """Lee un fichero que contiene un único polinomio en una línea."""
    try:
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
