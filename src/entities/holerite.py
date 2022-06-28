from src.business.tributos import Tributos
from src.entities.funcionario import Funcionario
from conexao_bd import gerar_cnx


class Holerite():

    def __init__(self, funcionario: Funcionario):
        self.matricula = funcionario.matricula
        self.funcionario = funcionario.nome
        self.data_admissao = funcionario.data_admissao
        self.cargo = funcionario.cargo_descricao()
        self.salario_base = funcionario.cargo_salario_base()
        self.comissao = float(funcionario.cargo_comissao_valor())
        self.valor_comissao = round(
            float(self.funcionario.cargo_salario_base()) * self.comissao / 100, 2)
        self.tributos = Tributos(funcionario.salario_base, funcionario.comissao)
        self.valor_inss = self.tributos.inss_recolhimento()
        self.valor_irrf = self.tributos.irrf_recolhimento()
        self.tx_inss = self.tributos.inss_aliquota
        self.tx_irff = self.tributos.irrf_aliquota
        self.total_vencimentos = funcionario.
        self.total_descontos = ''
        self.liquido_receber = ''
        self.base_inss = ''
        self.base_irrf = ''
        self.base_fgts = ''
        self.valor_fgts = ''

    def gerar_holerite(self, mes_ano: str, faltas: int) -> None:
        self.faltas = faltas
        self.valor_faltas = ''
        pass

    def holerites_cadastradas(self) -> None:
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        cursor.execute(
            f"SELECT * FROM cargos WHERE matricula = {self.matricula};")
        holerites_do_funcionario = cursor.fetchall()
        cursor.close()
        cnx.close()
        for holerite in holerites_do_funcionario:
            for chave, valor in holerite.items():
                print(f'| {chave}: {valor}', end='')
        print()

    def imprimir_holerite(self, mes_ano: str) -> None:
        print(f"""
__________________________________________________________________________________________       
Empresa XPTO Alimentos                          Recibo de Pagamento de Salário
Endereço: Rua XV de Novembro, 15, Centro        Mês de referência: {mes_ano}
CNPJ: 12.345.678/0001-00
==========================================================================================
Matricula     Nome do Funcionário       Data de Admissão        Função
{self.funcionario.matricula()}   {self.funcionario.nome}        {self.funcionario.data_de_admissao}          {self.funcionario.cargo_descricao()}
==========================================================================================
Código    Descrição                 Referência      Proventos         Descontos
   101    Salário Base                   22,50      R$ {self.funcionario.cargo_salario_base()}              
   203    Comissão                          {self.comissao}%      R$ {self.valor_comissao}
   303    Faltas                            {self.faltas}                   {self.valor_faltas}
   973    INSS Folha                       {self.tx_inss}                   {self.valor_inss}
   978    IRRF Folha                       {self.tx_irff}                   {self.valor_irrf}
   
   
                                                    Total Vencimentos   Total Descontos
                                                          R$ {self.total_vencimentos}      R$ {self.total_descontos}  
   
SalárioBase  BaseCálc.INSS  BaseCálc.FGT  FGTSmês  BaseCálcIRRF     Líquido a Receber: 
R$ {self.funcionario.cargo_salario_base()}   R$ {self.base_inss}   R$ {self.base_fgts}   R$ {self.valor_fgts} R$ {self.valor_irrf}    R$ {self.liquido_receber}         
""")
