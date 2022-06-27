from conexao_bd import gerar_cnx


class CadastroFuncionario():

    def __init__(self, nome: str, cpf: str, data_admissao: str, cargo: str, comissao=False):
        self.nome = nome
        self.cpf = cpf
        self.data_admissao = data_admissao
        self.cargo = cargo
        self.comissao = comissao

    def inclusao(self) -> None:
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        insert_query = "INSERT INTO funcionarios(nome,cpf,data_admissao,cargo,comissao) VALUES (%s,%s,%s,%s,%s)"
        insert_record = (self.nome, self.cpf, self.data_admissao,
                         self.cargo, self.comissao)
        cursor.execute(insert_query, insert_record)
        cnx.commit()

        insert_query = "SELECT matricula FROM funcionarios ORDER BY matricula DESC LIMIT 1;"
        cursor.execute(insert_query)
        self.matricula = cursor.fetchall()[0][0]
        cursor.close()
        cnx.close()

    def consultar_por_matricula(self, numero):
        
        entidade = list(filter(lambda x: x.id == id, self.__lista))

    # def remover_por_id(self, id: str) -> None:
    #     entidade = self.consultar(id)
    #     self.__lista.remove(entidade)

    def listagem():
        cnx = gerar_cnx()
        cursor = cnx.cursor(dictionary=True)
        insert_query = "SELECT * FROM funcionarios;"
        cursor.execute(insert_query)
        funcionarios_list_dict = cursor.fetchall()
        cursor.close()
        cnx.close()
        return funcionarios_list_dict

    # def funcao(self) -> None:
    #     cnx = gerar_cnx
    #     cursor = gerar_cursor

    #     salvar_commit()
    #     fechar_cursor()
    #     fechar_cnx()
