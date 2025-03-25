class Polinomio: #creamos un diccionario nueva para almacenar los polinomios
    def __init__(self, coeficientes):
        """Inicializa un polinomio a partir de un diccionario {grado: coeficiente}."""
        self.coeficientes = coeficientes
    def __str__(self):
        """Devuelve la representación en cadena del polinomio."""
        return " + ".join([f"{coef}x^{grado}" if grado > 1 else (f"{coef}x" if grado == 1 else f"{coef}") for grado, coef in sorted(self.coeficientes.items(), reverse=True)])

    def evaluar(self, x):
        """Evalúa el polinomio en un valor x dado."""
        resultado = sum(coef * (x ** grado) for grado, coef in self.coeficientes.items())
        return resultado

    def suma(self, otro):
        """Realiza la suma de dos polinomios."""
        resultado = self.coeficientes.copy()
        for grado, coef in otro.coeficientes.items():
            resultado[grado] = resultado.get(grado, 0) + coef
        return Polinomio(resultado)

    def resta(self, otro):
        """Realiza la resta de dos polinomios."""
        resultado = self.coeficientes.copy()
        for grado, coef in otro.coeficientes.items():
            resultado[grado] = resultado.get(grado, 0) - coef
        return Polinomio(resultado)

    def multiplicacion(self, otro):
        """Realiza la multiplicación de dos polinomios."""
        resultado = {}
        for grado1, coef1 in self.coeficientes.items():
            for grado2, coef2 in otro.coeficientes.items():
                nuevo_grado = grado1 + grado2
                resultado[nuevo_grado] = resultado.get(nuevo_grado, 0) + coef1 * coef2
        return Polinomio(resultado)

    def division(self, otro):
            if max(otro.coeficientes.keys()) == 0 and otro.coeficientes[0] == 0: #por si la división da una indeterminación
                return "Error: División por cero"

            dividendo = self.coeficientes.copy()
            divisor = otro.coeficientes
            cociente = {}

            if max(divisor.keys()) == 0: #así optimizamos computo, porque no hace falta la parte de exponentes
                coef_divisor = divisor[0]
                cociente = {grado: coef / coef_divisor for grado, coef in dividendo.items()}
                return Polinomio(cociente), Polinomio({})

            while dividendo and (max(dividendo.keys()) >= max(divisor.keys())):
                grado_dif = max(dividendo.keys()) - max(divisor.keys())
                coef_dif = dividendo[max(dividendo.keys())] / divisor[max(divisor.keys())]
                cociente[grado_dif] = coef_dif
                resta_polinomio = {grado + grado_dif: coef * coef_dif for grado, coef in divisor.items()}
                dividendo = Polinomio(dividendo).resta(Polinomio(resta_polinomio)).coeficientes
                dividendo = {k: v for k, v in dividendo.items() if v != 0}

            return Polinomio(cociente), Polinomio(dividendo) #el dividendo es el resto

def cargar_polinomio_desde_texto(texto):
    """Convierte un polinomio en formato texto a un diccionario."""
    coeficientes = {}
    texto = texto.replace("-", " -").replace("+", " +")
    terminos = texto.strip().split()
    for termino in terminos:
        if not termino:
            continue
        if "x^" in termino:
            coef_str, grado_str = termino.split("x^")
            coef_str = coef_str.strip()
            if coef_str not in ["", "+", "-"]:
                coef = float(coef_str)
            else:
                coef=float(coef_str + "1")
            grado = int(grado_str.strip())
        elif "x" in termino:
            coef_str = termino.replace("x", "").strip()
            if coef_str not in ["", "+", "-"]:
                coef = float(coef_str)
            else:
                coef=float(coef_str + "1")
            grado = 1
        else:
            if termino in ["", "+", "-"]:
                coef = float(termino + "1")
            else:
                coef = float(termino)
            grado = 0
        coeficientes[grado] = coef
    return Polinomio(coeficientes)
