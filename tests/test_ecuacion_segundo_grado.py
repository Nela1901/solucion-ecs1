"""Módulo de pruebas unitarias para la clase EcuacionSegundoGrado."""

import unittest
from src.logica.ecuacion_segundo_grado import EcuacionSegundoGrado

class TestEcuacionSegundoGrado(unittest.TestCase):
    """Pruebas para EcuacionSegundoGrado."""

    def test_solucion_esg_parametros_numericos_raices_reales(self):
        """Prueba de raíces reales con parámetros numéricos."""
        # Arrange
        parametro_a = 1
        parametro_b = -3
        parametro_c = 2
        ecuacion_segundo_grado = EcuacionSegundoGrado(parametro_a, parametro_b, parametro_c)

        raiz_esperada1 = 2.0
        raiz_esperada2 = 1.0

        # Act
        raiz_actual1, raiz_actual2 = ecuacion_segundo_grado.solucion_ecs()

        # Assert
        self.assertEqual(raiz_esperada1, raiz_actual1)
        self.assertEqual(raiz_esperada2, raiz_actual2)

    def test_solucion_esg_parametros_numericos_raices_complejas(self):
        """Prueba de raíces complejas con parámetros numéricos."""
        # Arrange
        parametro_a = 1
        parametro_b = 2
        parametro_c = 5
        ecuacion = EcuacionSegundoGrado(parametro_a, parametro_b, parametro_c)

        raiz_esperada1 = "-1.00+2.00i"
        raiz_esperada2 = "-1.00-2.00i"

        # Act
        raiz_actual1, raiz_actual2 = ecuacion.solucion_ecs()

        # Assert
        self.assertEqual(raiz_esperada1, raiz_actual1)
        self.assertEqual(raiz_esperada2, raiz_actual2)

if __name__ == "__main__":
    unittest.main()
