import unittest

from questao_02 import *

class TestPercec(unittest.TestCase):

    def test_percentual_venda(self):
        situacao1 = [(1, 1, 4), (1, 2, 3), (1, 3, 1), (2, 1, 3)]

        r_esperado = [(1, 0.6365), (2, 0.2727), (3, 0.0909), (4, 0)]

        self.assertEqual(percentual_vendas(situacao1), r_esperado)
