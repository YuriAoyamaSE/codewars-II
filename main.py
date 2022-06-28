from conexao_bd import gerar_cnx
from src.business.cadastro_funcionario import CadastroFuncionario
from src.entities.funcionario import Funcionario


def menu():
    print("""
Menu:
[1] - Cadastrar novo funcionário
[2] - Procurar dados de um funcionário
[3] - Listar todos os funcionários
[4] - Excluir funcionário
[5] - Alterar dados de um funcionário
[6] - Gerar holeritie de um funcionário
[7] - Gerar lista de holerities de todos os funcionários
[0] - Sair
          """)
    return input()

def cadastrar_funcionario():
    pass

def procurar_funcionario():
    pass
def listar_funcionarios():
    pass
def excluir_funcionario():
    pass
def alterar_funcionario():
    pass
def holerite_funcionario():
    pass
def listar_holerites():
    pass

if __name__ == '__main__':
    cadastro = CadastroFuncionario()
    opcao = ''
    while opcao != '0':
        opcao = menu()
        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            procurar_funcionario()
        elif opcao == '3':
            listar_funcionarios()
        elif opcao == '4':
            excluir_funcionario()
        elif opcao == '5':
            alterar_funcionario()
        elif opcao == '6':
            holerite_funcionario()
        elif opcao == '7':
            listar_holerites()        
        else:
            print('opção inválida, tente de novo.')

    print("""
          
--------------------------------Programa encerrado--------------------------------

          """)
