import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")

    def test_retorna_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_numero_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertGreater(len(resumen), 10)

    def test_valores_numericos_y_positivos(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        for total in resumen.values():
            self.assertIsInstance(total, float)
            self.assertGreaterEqual(total, 0)

    def test_provincia_existente(self):
        valor = self.analizador.ventas_por_provincia("pichincha")
        self.assertGreater(valor, 0)

    def test_provincia_inexistente(self):
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("Narnia")

if __name__ == "__main__":
    unittest.main()
