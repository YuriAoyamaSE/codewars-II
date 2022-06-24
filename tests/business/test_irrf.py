from unittest import TestCase
from src.business.tributos import Tributos


class TestIrrf(TestCase):
    
    def test_base_calculo(self):
        # dado
        vencimento = 3090

        # quando
        tributo = Tributos(vencimento)
        resultado = tributo.irff_base_calculo()

        # então
        self.assertTrue(resultado == 2821)

        
    def test_recolhimento(self):
        # dado
        base_calculo = 2821

        # quando
        tributo = Tributos(base_calculo)
        resultado = tributo.irff_recolhimento()

        # então
        self.assertTrue(resultado == 68.78)

