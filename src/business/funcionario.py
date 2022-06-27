 
import mysql.connector
from src.entities.funcionario import Funcionario
from .cadastro_abstract import FuncionarioAbtract


class Cadastrofuncionario(FuncionarioAbtract):


    def inserir(self, funcionario: Funcionario) -> None:
        cnx = mysql.connector.connect(user='root', password='123456',
                                      host='127.0.0.1',
                                      database='mydb')
        cursor = cnx.cursor()
        adiciona_funcionario = ("INSERT INTO Funcionario "
                            "(matricula, nome, data_de_admissao, cpf, cargo, comissao, cargo_codigo)"
                            " VALUES ( %(matricula)s, %(nome)s, %(data_de_admissao)s, %(cpf)s, %(cargo)s, %(comissao)s, %(cargo_codigo)s)")

        cursor.execute(adiciona_funcionario, {
            "matricula" : funcionario.matricula,
            "nome": funcionario.nome,
            "data_de_admissao": funcionario.data_de_admissao,
            "cpf": funcionario.cpf,
            "cargo": funcionario.cargo,
            "comissao" : funcionario.comissao,
            "cargo_codigo" : funcionario.cargo_codigo,
            
        })
        cnx.commit()

        cursor.close()
        cnx.close()

    def consultar(self, matricula: str) -> Funcionario:
        try:
            return super().consultar(matricula)
        except NotFoundError:
            raise FuncionarioNotFoundError('Funcionario não encontrado.')
        cnx = mysql.connector.connect(user='root', password='123456',
                                      host='127.0.0.1',
                                      database='mydb')
        cursor = cnx.cursor()

        query = ("SELECT matricula nome data_de_admissao cpf cargo comissao cargo_codigo FROM funcionario WHERE matricula=%s")

        cursor.execute(query, [matricula])

        for (matricula, nome, data_de_admissao, cpf, cargo comissao, cargo_codigo) in cursor:
           
        else:
            raise ClienteNotFoundError("Cliente não encontrado.")

        cursor.close()
        cnx.close()

        return funcionario
