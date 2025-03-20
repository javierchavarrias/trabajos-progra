class Polinomio: #creamos un diccionario nueva para almacenar los polinomios
    def __init__(self, coeficientes):
        """Inicializa un polinomio a partir de un diccionario {grado: coeficiente}."""
        self.coeficientes = coeficientes
    def __str__(self):
        """Devuelve la representación en cadena del polinomio."""
        return " + ".join([f"{coef}x^{grado}" if grado > 1 else (f"{coef}x" if grado == 1 else f"{coef}") for grado, coef in sorted(self.coeficientes.items(), reverse=True)])
git add .
git commit -m "Añadiendo archivos nuevos"
git push origin main

