from conexao_bd import gerar_cnx


class Funcionario():

    def __init__(self, nome: str, cpf: str, data_admissao: str, cargo: str, comissao: bool):
        self.nome = nome
        self.cpf = cpf
        self.data_admissao = data_admissao
        self.cargo = cargo
        self.comissao = comissao
        self.matricula = 'Funcionário não cadastrado'

    def __str__(self):
        return self.nome
    
    def cargo_descricao(self) -> str:
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        cursor.execute(
            f"SELECT descricao FROM cargos WHERE codigo = {self.cargo};")
        output = cursor.fetchall()
        cursor.close()
        cnx.close()
        return output

    def cargo_salario_base(self) -> str:
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        cursor.execute(
            f"SELECT salario_base FROM cargos WHERE codigo = {self.cargo};")
        output = cursor.fetchall()
        cursor.close()
        cnx.close()
        return output

    def cargo_comissao_valor(self) -> str:
        if self.__comissao:
            cnx = gerar_cnx()
            cursor = cnx.cursor()
            cursor.execute(
                f"SELECT comissao FROM cargos WHERE codigo = {self.cargo};")
            output = cursor.fetchall()
            cursor.close()
            cnx.close()
            return output
        return '0'
