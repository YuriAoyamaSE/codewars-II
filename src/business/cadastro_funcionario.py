from conexao_bd import gerar_cnx, gerar_cursor, fechar_cnx, fechar_cursor, salvar_commit


class CadastroFuncionario():

    def __init__(self, nome: str, cpf: str, data_admissao: str, cargo: str, comissao=False):
        self.nome = nome
        self.cpf = cpf
        self.data_admissao = data_admissao
        self.cargo = cargo
        self.comissao = comissao

    def inclusao(self) -> None:
        cnx = gerar_cnx()
        cursor = gerar_cursor(cnx)
        insert_query = "INSERT INTO codewars2.funcionarios(nome,cpf,data_admissao,cargo,comissao) VALUES (%s,%s,%s,%s,%s)"
        insert_record = (self.nome, self.cpf, self.data_admissao,
                         self.cargo, self.comissao)
        cursor.execute(insert_query, insert_record)
        salvar_commit(cnx)

        insert_query = f"SELECT matricula FROM codewars2.funcionarios ORDER BY matricula DESC LIMIT 1;"
        cursor.execute(insert_query)
        self.matricula = cursor.fetchall()[0][0]
        fechar_cursor(cursor)
        fechar_cnx(cnx)

    # def consultar(self, id: str):
    #     entidade = list(filter(lambda x: x.id == id, self.__lista))

    # def remover_por_id(self, id: str) -> None:
    #     entidade = self.consultar(id)
    #     self.__lista.remove(entidade)

    # def listar_todos(self) -> :
    #     return self.__lista

    # def funcao(self) -> None:
    #     cnx = gerar_cnx
    #     cursor = gerar_cursor

    #     salvar_commit()
    #     fechar_cursor()
    #     fechar_cnx()
