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