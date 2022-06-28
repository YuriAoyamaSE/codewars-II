from conexao_bd import gerar_cnx


class Funcionario():

    def __init__(self, nome: str, cpf: str, data_de_admissao: str, cargo: str, comissao: bool):
        self.nome: str = nome
        self.cpf: str = cpf
        self.data_de_admissao: str = data_de_admissao
        self.cargo: str = cargo
        self.comissao: str = comissao

    def __str__(self):
        return self.nome
    
    def matricula(self):
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        cursor.execute(
            f"SELECT matricula FROM funcionarios WHERE cpf = {self.cpf};")
        output = cursor.fetchall()
        cursor.close()
        cnx.close()
        return output
    
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
