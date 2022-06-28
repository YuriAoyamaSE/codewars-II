# codewars-II

## PROJETO INCOMPLETO:
### => Funcionalidade de holerite em construção
### => BD de holerite em construção (criado, não testado)
### => Sem tratamento de exceções
### => Funcionando: Sistema de cadastro de funcionários, cálculos de tributos, BD de funcionários, BD de cargos, funcionalidades respectivas.
### => Funcionando parcial: main.py, menos a parte de holerites.


## Observações:
### => Necessário um arquivo .env com dados de conexão com um BD (mySQL)

        NAME='[nome do bd]'        
        USER='[nome do usuário do bd]'        
        PASSWORD='[senha do usuário]'        
        HOST='[ip do host]'        
        PORT='[porta de acesso]'

### => Necessário gerar um BD, podendo executar os arquivos gerar_bd.py e gerar_cargos.py (molde: mysql)
Contanto que o arquivo .env seja criado e preenchido com os dados sensíveis acima, rodar o arquivo gerar_bd.py vai criar os Bancos de Dados necessários para testar o projeto.
Serão criados três BD, dentro de um Schema 'codewars2': 'funcionarios', 'cargos' e 'holerites'.
Por sua vez, rodar o arquivo gerar_cargos.py vai preencher o BD 'cargos' com os cargos apresentados no exercício (conforme Holerities.xlsx).

### => O valor das faltas não foi especificado na documentação. Aplicado proporcional com o exemplo ([número de faltas] x [salário base] x [0.75] x [22.5])
75% em relação ao salário base
22.5 foi a referência dada por dias de trabalho em um mês
