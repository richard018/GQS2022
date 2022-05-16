import unittest

from questao_01 import *


class TestProduto(unittest.TestCase):
    def test_lista_produtos(self):
        situacao1 = [('Shampoo', 10), ('Condicionador', 5), ('Sabonete', 2)]
        situacao2 = [('Shampoo', 10), ('Condicionador', 5), ('Sabonete', 5)]
        situacao3 = []

        self.assertEqual(reposicao(situacao1), 2)
        self.assertEqual(reposicao(situacao2), 1)
        self.assertEqual(reposicao(situacao3), 0)
