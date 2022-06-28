

"""
1. Gerar o holerite de um funcionário específico
  - solicitar o mês
  - definir campo chave para busca, apresentar os dados pessoais do funcionário, solicitar a quantidade de faltas, gerar e apresentar o holerite
  - armazenar o holerite do funcionário no banco de dados
  - apresentar mensagem de erro caso a chave de busca não seja encontrada (Exceções)

2. Gerar o holerite de todos os funcionários
  - solicitar o mês
  - gerar holerite apenas dos funcionários que ainda não possuem holerite do mês
  - considerar que estes funcionários não tiveram falta (automaticamente, considerar 22,5 dias trabalhados)
  - apresentar o holerite do mês de todos os funcionários
  - emitir mensagem de erro caso não hajam funcionários cadastrados (Exceções)
"""

from src.entities.funcionario import Funcionario


class Holerites():

    def __init__(self, funcionario: Funcionario) -> None:
        self.funcionario = funcionario
    
    def gerar_holerite(self, mes: str, faltas: int):
        pass
    
    def listar_holerites(mes):
        pass

    def imprimir_holerite(self, mes):
        faltas = ''        
        tx_inss =''
        tx_irff =''
        comissao= int('')
        valor_comissao=round(int(self.funcionario.cargo_salario_base()) * comissao /100, 2)
        valor_faltas = ''
        valor_inss = ''
        valor_irrf =''
        total_vencimentos=''
        total_descontos=''
        liquido_receber=''
        base_inss=''
        base_irrf=''
        base_fgts=''
        valor_fgts=''
        print(f"""
__________________________________________________________________________________________       
Empresa XPTO Alimentos                          Recibo de Pagamento de Salário
Endereço: Rua XV de Novembro, 15, Centro        Mês de referência: {mes}
CNPJ: 12.345.678/0001-00
==========================================================================================
Matricula     Nome do Funcionário       Data de Admissão        Função
{self.funcionario.matricula()}   {self.funcionario.nome}        {self.funcionario.data_de_admissao}          {self.funcionario.cargo_descricao()}
==========================================================================================
Código    Descrição                 Referência      Proventos         Descontos
   101    Salário Base                   22,50      R$ {self.funcionario.cargo_salario_base()}              
   203    Comissão                          {comissao}%      R$ {valor_comissao}
   303    Faltas                            {faltas}                   {valor_faltas}
   973    INSS Folha                       {tx_inss}                   {valor_inss}
   978    IRRF Folha                       {tx_irff}                   {valor_irrf}
   
   
                                                    Total Vencimentos   Total Descontos
                                                          R$ {total_vencimentos}      R$ {total_descontos}  
   
SalárioBase  BaseCálc.INSS  BaseCálc.FGT  FGTSmês  BaseCálcIRRF     Líquido a Receber: 
R$ {self.funcionario.cargo_salario_base()}   R$ {base_inss}   R$ {base_fgts}   R$ {valor_fgts} R$ {valor_irrf}    R$ {liquido_receber}         
""")