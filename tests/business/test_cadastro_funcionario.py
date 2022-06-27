from unittest import TestCase
from src.business.cadastro_funcionario import CadastroFuncionario
from conexao_bd import gerar_cnx, gerar_cursor, fechar_cnx, fechar_cursor, salvar_commit


class TestInss(TestCase):

    @classmethod
    def setUpClass(self):
        # dado
        self.cadastro1 = CadastroFuncionario(
            'fulano1', '12345678900', '2022-06-06', '10', True)
        self.cadastro2 = CadastroFuncionario(
            'fulano2', '22345678900', '2022-07-06', '30', True)
        self.cadastro3 = CadastroFuncionario(
            'fulano3', '32345678900', '2022-08-06', '50', False)

    def inclusao(self):
        # dado
        cnx = gerar_cnx()
        cursor = gerar_cursor()
        cursor.rowcount()
        fechar_cursor()
        fechar_cnx() 
        
        # quando

        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 82.50)

    def exclusao(self):
        # dado
        vencimentos = 1_100

        # quando
        tributo = Tributos(vencimentos)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 82.50)

    def consulta(self):
        # dado
        vencimentos = 1_100

        # quando
        tributo = Tributos(vencimentos)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 82.50)

    def alteracao(self):
        # dado
        vencimentos = 1_100

        # quando
        tributo = Tributos(vencimentos)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 82.50)

    def listagem(self):
        # dado
        vencimentos = 1_100

        # quando
        tributo = Tributos(vencimentos)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 82.50)
