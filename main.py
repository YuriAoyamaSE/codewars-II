from src.business.cadastro_funcionario import CadastroFuncionario
from src.entities.funcionario import Funcionario
from src.entities.holerite import Holerite


def menu():
    print("""----------------------Menu----------------------
[1] - Cadastrar novo funcionário
[2] - Procurar dados de um funcionário
[3] - Listar todos os funcionários
[4] - Excluir funcionário
[5] - Alterar dados de um funcionário
[6] - Gerar holeritie de um funcionário
[7] - Gerar lista de holerities de todos os funcionários
[0] - Sair""")
    return input()


def cadastrar_funcionario():
    print('-----------Cadastro de novo funcionário-----------')
    nome = input('Informe o nome: ')
    cpf = input('Informe o CPF (apenas números): ')
    data_admissao = input('Informe a data de admissão (aaaa-mm-dd): ')
    cargo = input('Informe o código do cargo: ')
    comissao = input('O funcionário receberá comissão? (s/n): ')
    comissao = True if comissao == 's' else False
    funcionario = Funcionario(nome, cpf, data_admissao, cargo, comissao)
    cadastro_funcionario.inclusao(funcionario)
    print('Cadastro efetuado com a matricula:', funcionario.matricula)


def checar_funcionario(matricula):
    funcionario = cadastro_funcionario.consulta(matricula)
    if funcionario:
        return funcionario
    else:
        print('Funcionário não encontrado')
        return None

def procurar_funcionario():
    print('-------------Procurar por funcionário-------------')
    matricula = int(input('Informe o número de matrícula: '))
    funcionario = checar_funcionario(matricula)
    if funcionario:
        for chave, valor in funcionario.items():
            print(f'{chave}: {valor}')


def listar_funcionarios():
    print('---------------Listar funcionários---------------')
    lista_funcionarios = cadastro_funcionario.listagem()
    for funcionario in lista_funcionarios:
        for chave, valor in funcionario.items():
            print(f'| {chave}: {valor}', end='')
        print()


def excluir_funcionario():
    print('---------------Excluir funcionário---------------')
    matricula = int(input('Informe o número de matrícula: '))
    funcionario = checar_funcionario(matricula)
    if funcionario:
        cadastro_funcionario.exclusao(matricula)


def alterar_funcionario():
    print('-----------Alterar dados de funcionário-----------')
    matricula = int(input('Informe o número de matrícula: '))
    funcionario = checar_funcionario(matricula)
    if funcionario:
        for chave, valor in funcionario.items():
            print(f'{chave}: {valor}')
            i += 1
        escolha = input(
            'Qual informação gostaria de alterar? Para sair, informe "0". ')
        alteracoes = {}
        while escolha != '0':
            if escolha in funcionario.keys():
                alteracoes[escolha] = input(f'{escolha}: ')
            else:
                print('Opção inválida.')
            escolha = input(
                'Qual informação gostaria de alterar? Para sair, informe "0". ')
        cadastro_funcionario.alteracao(matricula, alteracoes)



def holerite_funcionario():
    print('---------Imprimir holerite de funcionario----------')
    matricula = int(input('Informe o número de matrícula: '))
    if checar_funcionario(matricula):
        funcionario = cadastro_funcionario.retornar_funcionario(matricula)
        mes_ano = input('Informe o mês e ano da holerite: ')   
        holerite = Holerite(funcionario)
        holerite.gerar_holerite(mes_ano, 2)
        holerite.imprimir_holerite()


def listar_holerites():
    pass


if __name__ == '__main__':
    cadastro_funcionario = CadastroFuncionario()
    while True:
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
        elif opcao == '0':
            break
        else:
            print('opção inválida, tente de novo.')

    print("""          
--------------------------------Programa encerrado--------------------------------
          """)
