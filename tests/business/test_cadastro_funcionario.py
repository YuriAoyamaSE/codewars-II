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
        self.cadastro1.inclusao()
        self.cadastro2.inclusao()
        self.cadastro3.inclusao()

    def inclusao(self):
        # dado
        cadastro4 = CadastroFuncionario(
            'fulano4', '42345678900', '2022-09-06', '10', False)
        cnx = gerar_cnx()
        cursor = gerar_cursor(cnx)
        operacao = "SELECT * FROM codewars2.cargos"

        # quando
        cadastro4.inclusao()
        cursor.execute(operacao)
        resultado = cursor.rowcount()
        fechar_cursor(cursor)
        fechar_cnx(cnx)

        # então
        self.assertTrue(resultado == 4)

    def exclusao(self):
        pass

    def consulta(self):
        pass

    def alteracao(self):
        pass

    def listagem(self):
        pass
