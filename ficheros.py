import polinomios
def leer_fichero_completo(nombre_fichero):
    """Lee un fichero que contiene todo el funcionamiento"""
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
        resultado = None
        p1 = polinomios.cargar_polinomio_desde_texto(datos['p1'])
        if datos['operacion'] == 'EVALUACIÓN':
                resultado = p1.evaluar(datos['numero'])
        else:
            p2 = polinomios.cargar_polinomio_desde_texto(datos['p2'])
            if datos['operacion'] == 'SUMA':
             resultado = p1.suma(p2)
            elif datos['operacion'] == 'RESTA':
                    resultado = p1.resta(p2)
            elif datos['operacion'] == 'MULTIPLICACION':
                    resultado = p1.multiplicacion(p2)
            elif datos['operacion'] == 'DIVISION':
                    resultado, resto = p1.division(p2)
                    datos['resto'] = resto
            datos['resultado'] = resultado
            return datos
    except FileNotFoundError:
        print("Error: Fichero no encontrado.")
        return None

def leer_fichero_unico(nombre_fichero):
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
