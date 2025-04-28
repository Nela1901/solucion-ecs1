"""Módulo que resuelve ecuaciones de segundo grado, reales o complejas."""

import math

class EcuacionSegundoGrado:
    """Clase que representa una ecuación de segundo grado."""

    def __init__(self, a, b, c):
        """Inicializa los parámetros de la ecuación."""
        self.a = a
        self.b = b
        self.c = c

    def definir_parametros(self, parametro_a, parametro_b, parametro_c):
        """Define nuevos valores para los parámetros de la ecuación."""
        self.a = parametro_a
        self.b = parametro_b
        self.c = parametro_c

    def solucion_ecs(self):
        """Calcula las soluciones de la ecuación de segundo grado."""
        discriminante = math.pow(self.b, 2) - 4 * self.a * self.c
        if discriminante >= 0:  # Solo calculamos si las raíces son reales
            raiz_discriminante = math.sqrt(discriminante)
            x1 = (-self.b + raiz_discriminante) / (2 * self.a)
            x2 = (-self.b - raiz_discriminante) / (2 * self.a)
            return x1, x2

        # Soluciones complejas
        parte_real = -self.b / (2 * self.a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2 * self.a)
        x1 = f"{parte_real:.2f}+{parte_imaginaria:.2f}i"
        x2 = f"{parte_real:.2f}-{parte_imaginaria:.2f}i"
        return x1, x2

    def imprimir_raices(self):
        """Imprime las soluciones de la ecuación."""
        print("\nEcuación de segundo grado")
        print(f"{self.a:.2f}X^2 + {self.b:.2f}x + {self.c:.2f}")
        print("\nSolución:")
        x1, x2 = self.solucion_esg()
        print(f"X1 = {x1}")
        print(f"X2 = {x2}")
