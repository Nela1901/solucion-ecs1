import unittest
import math
from src.logica.ecuacion_segundo_grado import EcuacionSegundoGrado

class TestEcuacionSegundoGrado(unittest.TestCase):
    def test_solucionESG_parametrosNumericos_raicesReales(self):
        # Arrange
        ecuacionSegundoGrado=EcuacionSegundoGrado()
        parametroA = 1
        parametroB = 1
        parametroC = 1

        RaizEsperada1 = "1.43"
        RaizEsperada2 = "0.23"

        # Do
        ecuacionSegundoGrado.definirParametros(parametroA, parametroB, parametroC)
        RaizActual1, RaizActual2 = ecuacionSegundoGrado.solucionESG()

        # Assert
        self.assertEqual(RaizEsperada1, RaizActual1)
        self.assertEqual(RaizEsperada2, RaizActual2)



