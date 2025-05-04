def principal():
# CDB - investimento do cliente no banco
    valor_investido = float(input("Digite o valor para simular no CDB e no CDC: "))
    periodo_cdb = float(input("Digite o período (em anos) da aplicação do CDB: "))
    taxa_anual_percentual_cdb = float(input("Digite a taxa percentual anual (entre 1% a 20%) da aplicação no CDB: "))

    montante_cdb = simulador_CDB(valor_investido, taxa_anual_percentual_cdb, periodo_cdb)
    juros_cdb = calcular_juros(simulador_CDB(valor_investido, taxa_anual_percentual_cdb, periodo_cdb), valor_investido)
    
    print('')

# CDC - empréstimo do banco ao cliente
    taxa_mensal_percentual_cdc = int(input("Digite a taxa percentual do CDC (entre 1% e 17% aos mês): "))
    periodo_cdc = int(input("Digite o prazo, em meses, para o pagamento (prazos comuns: 24x, 36x, 60x): "))

    print(f"""       
    |         OPERAÇÃO DE CERTIFICADO DE DEPÓSITO BANCÁRIO EFETIVADA!!!
    |      
    |O valor investido R$ {valor_investido:.2f},
    |rendendo durante {periodo_cdb} anos, com uma taxa anual de {taxa_anual_percentual_cdb}% ao ano 
    |sobre o valor, em juros compostos, gera R$ {juros_cdb:.2f} de juros 
    |e um montante de R$ {montante_cdb:.2f} !!
    ------------------------------------------------------------------------------\n""")

    montante_cdc = simulador_CDC(valor_investido, taxa_mensal_percentual_cdc, periodo_cdc)
    juros_cdc = calcular_juros(montante_cdc, valor_investido)

    print (f"""
    |         OPERAÇÃO DE CRÉDITO DIRETO AO CONSUMIDOR EFETIVADA!!!
    |O valor de R$ {valor_investido:.2f} do empréstimo,
    |com o prazo de {periodo_cdc} meses para o pagamento ocorrendo uma taxa de {taxa_mensal_percentual_cdc} ao mês,
    |resultará em R$ {juros_cdc:.2f} de juros e um montante de R$ {montante_cdc:.2f}. 
    |O cliente decidiu pagar em {periodo_cdc}x de R$ {montante_cdc / periodo_cdc:.2f}!!
    ------------------------------------------------------------------------------\n""")

# Saída das transações com o lucro bancário
    lucro_banco = calcular_lucro_banco(juros_cdb, juros_cdc)

    print (f"""
            >>>>> NOTA FISCAL COMPLETA <<<<<
       
    --> OPERAÇÃO: CERTIFICADO DE DEPÓSITO BANCÁRIO (CDB)
        Valor investido: R${valor_investido:.2f}
        Período: {periodo_cdb} ano(s)   Taxa percentual: {taxa_anual_percentual_cdb}% a.a
        Juros: R${juros_cdb:.2f}        Montante: R${montante_cdb:.2f}

    --> OPERAÇÃO: CRÉDITO DIRETO AO CONSUMIDOR (CDC)
        Valor investido: R${valor_investido:.2f}
        Prazo: {periodo_cdc} mês(es)    Taxa percentual: {taxa_mensal_percentual_cdc}% a.m
        Juros: R${juros_cdc:.2f}        Montante: R${montante_cdc:.2f}
        Qtde de parcelas: {periodo_cdc} Valor da parcela: R${montante_cdc / periodo_cdc:.2f}

    --> LUCRO BANCÁRIO DAS OPERAÇÕES = R${lucro_banco:.2f}

""")


def simulador_CDB(valor_investido, taxa_anual_percentual, periodo):
    montante_cdb = calcular_juros_compostos(valor_investido, taxa_anual_percentual, periodo)
# o montante é quanto o banco irá pagar ao cliente no final do período
    return montante_cdb


def simulador_CDC(valor_emprestado, taxa_mensal_percentual, periodo_cdc):
    montante_cdc = calcular_juros_compostos(valor_emprestado, taxa_mensal_percentual, periodo_cdc)
    valor_parcela = montante_cdc / periodo_cdc
    return montante_cdc


def calcular_juros_compostos(capital, taxa, tempo):
    montante = capital * (1 + (taxa/100))** tempo
    return montante


def calcular_juros(montante, capital):
    juros = montante - capital
    return juros


def calcular_lucro_banco (juros_cdb, juros_cdc):
    lucro_banco = juros_cdc - juros_cdb
    return lucro_banco


principal()