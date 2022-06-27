from conexao_bd import gerar_cnx, gerar_cursor, fechar_cnx, fechar_cursor, salvar_commit


class CadastroFuncionario():

    def __init__(self, nome: str, cpf: str, data_admissao, cargos_codigo: str, comissao=False):
        self.nome = nome
        self.cpf = cpf
        self.data_admissao = data_admissao
        self.cargos_codigo = cargos_codigo
        self.comissao = comissao

    def inclusao(self) -> None:
        cnx = gerar_cnx()
        cursor = gerar_cursor()
        
        self.matricula
        
        salvar_commit()
        fechar_cursor()
        fechar_cnx()
        

    def consultar(self, id: str) -> Entity:
        entidade = list(filter(lambda x: x.id == id, self.__lista))

    def remover_por_id(self, id: str) -> None:
        entidade = self.consultar(id)
        self.__lista.remove(entidade)

    def listar_todos(self) -> List[Entity]:
        return self.__lista
    
    def funcao(self) -> None:
        cnx = gerar_cnx
        cursor = gerar_cursor
        
        salvar_commit()
        fechar_cursor()
        fechar_cnx()