
class Tributos():

    def __init__(self, remuneracao) -> None:
        self.remuneracao = remuneracao

    def inss_aliquota() -> dict:
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
        aliquotas = Tributos.inss_aliquota()
        valor = self.remuneracao
        recolhimento = 0
        for faixa, aliquota in aliquotas.items():
            if faixa < valor:
                valor -= faixa
                recolhimento += round(faixa * aliquota, 2)
            else:
                recolhimento += round(valor * aliquota, 2)
                return recolhimento
        return recolhimento

    def irrf_base_calculo(self) -> float:
        pass

    def irrf_recolhimento(self) -> float:
        pass
