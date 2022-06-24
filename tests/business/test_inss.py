from unittest import TestCase
from src.business.tributos import Tributos


class TestInss(TestCase):

    def test_faixa_1(self):
        # dado
        remuneracao = 1_100

        # quando
        tributo = Tributos(remuneracao)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 8.40)

    def test_faixa_2(self):
        # dado
        remuneracao = 1_500

        # quando
        tributo = Tributos(remuneracao)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 116.82)

    def test_faixa_3(self):
        # dado
        remuneracao = 3_000

        # quando
        tributo = Tributos(remuneracao)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 269.00)

    def test_faixa_4(self):
        # dado
        remuneracao = 5_000

        # quando
        tributo = Tributos(remuneracao)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 536.18)

    def test_acima_do_teto(self):
        # dado
        remuneracao = 8_000

        # quando
        tributo = Tributos(remuneracao)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 828.39)
