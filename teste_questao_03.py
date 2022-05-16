import unittest

from questao3 import *

class TestVendasTotal(unittest.TestCase):
    def test_vendas_total(self):
        situacao01 = [(1, 50.50), (2, 200.95), (3, 20.95), (4, 100.40)]

        self.assertEqual(soma_vendas(situacao01), 372.8)