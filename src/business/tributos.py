
class Tributos():

    def __init__(self, salario_base, comissao=0) -> None:
        self.salario_base = salario_base
        self.comissao = comissao
        self.vencimentos = salario_base + comissao
        self.inss_aliquota = ''

    def inss_margem_aliquota(self) -> dict:
        faixa_aliquota = [0.075, 0.09, 0.12, 0.14]
        faixa_teto = [1212.00, 2427.35, 3641.03, 7087.22]
        margem_aliquota = {}
        for i in range(len(faixa_aliquota)):
            if i == 0:
                margem = faixa_teto[i]
            else:
                margem = faixa_teto[i]-faixa_teto[i-1]
            margem_aliquota[margem] = faixa_aliquota[i]
        return margem_aliquota

    def inss_recolhimento(self) -> float:
        aliquotas = self.inss_margem_aliquota()
        valor = self.vencimentos
        recolhimento = 0
        for faixa, aliquota in aliquotas.items():
            if faixa < valor:
                valor -= faixa
                recolhimento += faixa * aliquota
            else:
                recolhimento += valor * aliquota
                self.inss_aliquota = aliquota
                return round(recolhimento, 2)
        return round(recolhimento, 2)

    def irrf_parametros(self) -> dict:
        base_de_calculo = round(self.vencimentos - self.inss_recolhimento(), 2)
        if base_de_calculo <= 1903.98:
            aliquota = 0
            deducao = 0
        elif base_de_calculo <= 2826.65:
            aliquota = 0.075
            deducao = 142.80
        elif base_de_calculo <= 3751.05:
            aliquota = 0.15
            deducao = 354.80
        elif base_de_calculo <= 4664.68:
            aliquota = 0.225
            deducao = 636.13
        else:
            aliquota = 27.5
            deducao = 869.36
        return {'bc': base_de_calculo, 'aliquota': aliquota, 'deducao': deducao}

    def irrf_recolhimento(self) -> float:
        parametro = self.irrf_parametros()
        recolhimento = parametro['bc'] * \
            parametro['aliquota'] - parametro['deducao']
        return round(recolhimento, 2)
