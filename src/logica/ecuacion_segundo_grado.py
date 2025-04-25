import math

class EcuacionSegundoGrado:
    """Clase ecuacion de segundo grado"""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def definirParametros(self, parametroA, parametroB, parametroC):
        self.a = parametroA
        self.b = parametroB
        self.c = parametroC

    def solucionESG(self):
        """solucion de la ecuacion de segundo grado"""
        discriminante = math.pow(self.b, 2) - 4 * self.a * self.c
        if discriminante >= 0:  # Solo calculamos si las raíces son reales
            raizdiscriminante = math.sqrt(discriminante)
            x1 = (-self.b + raizdiscriminante) / (2 * self.a)
            x2 = (-self.b - raizdiscriminante) / (2 * self.a)
            return x1, x2
        else:
            return None, None  # No hay raíces reales

    def imprimir_raices(self):
        print("\nEcuación de segundo grado")
        print("{0:.2f}X^2 + {1:.2f}x + {2:.2f}".format(self.a, self.b, self.c))
        print("\nSolución:")
        x1, x2 = self.solucionESG()
        print(f"X1 = {x1}")
        print(f"X2 = {x2}")
