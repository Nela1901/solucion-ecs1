import unittest
import math
from src.logica.ecuacion_segundo_grado import EcuacionSegundoGrado

class TestEcuacionSegundoGrado(unittest.TestCase):
    def test_solucionESG_parametrosNumericos_raicesReales(self):
        # Arrange
        parametroA = 1
        parametroB = -3  # Cambié b a -3 para tener raíces reales
        parametroC = 2   # Cambié c a 2 para que el discriminante sea positivo

        # Crear la instancia de EcuacionSegundoGrado pasando los parámetros directamente
        ecuacionSegundoGrado = EcuacionSegundoGrado(parametroA, parametroB, parametroC)

        # Las raíces esperadas son 2 y 1 para la ecuación x^2 - 3x + 2 = 0
        RaizEsperada1 = 2.0
        RaizEsperada2 = 1.0

        # Do
        RaizActual1, RaizActual2 = ecuacionSegundoGrado.solucionESG()

        # Assert
        self.assertEqual(RaizEsperada1, RaizActual1)
        self.assertEqual(RaizEsperada2, RaizActual2)

if __name__ == "__main__":
    unittest.main()
