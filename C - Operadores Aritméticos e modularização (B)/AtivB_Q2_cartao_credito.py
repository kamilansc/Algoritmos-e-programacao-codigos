def principal():
    valor_fatura = float(input("Digite o valor da fatura: "))
    
    print("\n     >>> OPÇÕES DE PAGAMENTO <<<     ")
    print("--> Plano de pagamento 1: ")
    print(f"Opções aceitas: ( )Valor da fatura: R${valor_fatura:.2f}  ( )Qualquer valor abaixo de R${valor_fatura:.2f}")
    valor_pagar_1 = float(input("Digite o valor a ser pago no plano 1 de pagamento: "))
    qtd_meses_1 = int(input("Digite a quantidade de meses sem pagamento do plano 1: "))

    print("--> Plano de pagamento 2: ")
    print(f"Opções aceitas: ( )Valor da fatura: R${valor_fatura:.2f}  ( )Qualquer valor abaixo de R${valor_fatura:.2f}")
    valor_pagar_2 = float(input("Digite o valor a ser pago no plano 2 de pagamento: "))
    qtd_meses_2 = int(input("Digite a quantidade de meses sem pagamento do plano 2: "))

# Processamento da forma de pagamento 1:
    saldo_devedor_1 = valor_fatura - valor_pagar_1
    juros_rotativo_1 = calcular_juros_fatura(saldo_devedor_1, 12, qtd_meses_1)
    multa_atraso_1 = calcular_juros_fatura(saldo_devedor_1, 2, qtd_meses_1)
    juros_mora_1 = calcular_juros_fatura(saldo_devedor_1, 1, qtd_meses_1)

    fatura_opcao_1 = calcular_total_fatura(saldo_devedor_1, juros_rotativo_1, multa_atraso_1, juros_mora_1)
#    aumento_percentual_1 = crescimento_percentual_fatura(fatura_opcao_1, saldo_devedor_1)
    total_juros = juros_rotativo_1 + juros_mora_1 + multa_atraso_1

# Processamento da forma de pagamento 2:
    saldo_devedor_2 = valor_fatura - valor_pagar_2
    juros_rotativo_2 = calcular_juros_fatura(saldo_devedor_2, 12, qtd_meses_2)
    multa_atraso_2 = calcular_juros_fatura(saldo_devedor_2, 2, qtd_meses_2)
    juros_mora_2 = calcular_juros_fatura(saldo_devedor_2, 1, qtd_meses_2)

    fatura_opcao_2 = calcular_total_fatura(saldo_devedor_2, juros_rotativo_2, multa_atraso_2, juros_mora_2)
    total_juros_2 = juros_rotativo_2 + multa_atraso_2 + juros_mora_2    

# Novo saldo devedor após M meses sem pagar novamente
    # Plano de pagamento 1:
    nova_qtd_meses = int(input("Digite quantos meses você ficou sem pagar novamente: "))
    
    qtd_meses_total_1 = soma_meses(qtd_meses_1, nova_qtd_meses)
    novo_juros_rotativo_1 = calcular_juros_fatura(saldo_devedor_1, 12, qtd_meses_total_1)
    nova_multa_atraso_1 = calcular_juros_fatura(saldo_devedor_1, 2, qtd_meses_total_1)
    novo_juros_mora_1 = calcular_juros_fatura(saldo_devedor_1, 1, qtd_meses_total_1)
    
    nova_fatura_1 = calcular_total_fatura(saldo_devedor_1, novo_juros_rotativo_1, nova_multa_atraso_1, novo_juros_mora_1)
    novo_aumento_percentual_1 = crescimento_percentual_fatura(nova_fatura_1, saldo_devedor_1)

    # Plano de pagamento 2:
    qtd_meses_total_2 = soma_meses(qtd_meses_2, nova_qtd_meses)
    novo_juros_rotativo_2 = calcular_juros_fatura(saldo_devedor_2, 12, qtd_meses_total_2)
    nova_multa_atraso_2 = calcular_juros_fatura(saldo_devedor_2, 2, qtd_meses_total_2)
    novo_juros_mora_2 = calcular_juros_fatura(saldo_devedor_2, 1, qtd_meses_total_2)

    nova_fatura_2 = calcular_total_fatura(saldo_devedor_2, novo_juros_rotativo_2, nova_multa_atraso_2, novo_juros_mora_2)
    novo_aumento_percentual_2 = crescimento_percentual_fatura(nova_fatura_2, saldo_devedor_2)

# Saída:
    print(f"""
                    >>> PLANO DE PAGAMENTO 1 <<<
        Fatura postergada incial: R${fatura_opcao_1:.2f}        Total de juros adcionados: R${total_juros:.2f}
        ==> Obs.: Caso o valor acima seja = 0, significa que você pagou a fatura de acordo com o 
        plano 1 de pagamento definido!!
        
        
        --> DADOS ATUALIZADOS DA FATURA APÓS MAIS UM PERÍODO DE ATRASO:
        
            - ATENÇÃO: A fatura, inicialmente de R${fatura_opcao_1:.2f}, após mais {nova_qtd_meses} meses
            sem pagamento está AGORA NO VALOR de R${nova_fatura_1:.2f}. Logo abaixo mais detalhes:

            Saldo devedor: R${saldo_devedor_1:.2f};
                + Juros rotativo: R${novo_juros_rotativo_1:.2f}
                + Multa por atraso de {qtd_meses_total_1} meses: R${nova_multa_atraso_1:.2f}
                + Juros de mora: R${novo_juros_mora_1:.2f}
                > Percentual de crescimento fatura de R${nova_fatura_1:.2f} em relação ao saldo devedor de R${saldo_devedor_1:.2f}: {novo_aumento_percentual_1:.2f}%
            

                    >>> PLANO DE PAGAMENTO 2 <<<
        Fatura postergada inicial: R${fatura_opcao_2:.2f}       Total de juros adicionados: R$ {total_juros_2}
        ==> Obs.: Caso o valor acima seja = 0, significa que você pagou a fatura de acordo com o 
        plano 2 de pagamento definido!!

    
        --> DADOS ATUALIZADOS DA FATURA APÓS MAIS UM PERÍODO DE ATRASO:

            - ATENÇÃO: A fatura, inicialmente de R${fatura_opcao_2:.2f}, após mais {nova_qtd_meses} meses
            sem pagamento está AGORA NO VALOR de R${nova_fatura_2:.2f}. Logo abaixo mais detalhes:

            Saldo devedor: R${saldo_devedor_2:.2f}
                + Juros rotativo: R${novo_juros_rotativo_2:.2f}
                + Multa por atraso de {qtd_meses_total_2} meses: R$ {multa_atraso_2:.2f}
                + Juros de mora: R${novo_juros_mora_2:.2f}
                > Percentual de crescimento fatura de R${nova_fatura_2:.2f} em relação ao saldo devedor de R${saldo_devedor_2:.2f}: {novo_aumento_percentual_2:.2f}% """)

def calcular_juros_fatura(capital, taxa, tempo):
    montante = capital * (1+(taxa/100))**tempo
    return montante


def calcular_total_fatura (saldo_devedor, juros_rotativo, multa_atraso, juros_mora):
    total_fatura = saldo_devedor + juros_rotativo + multa_atraso + juros_mora
    return total_fatura


def soma_meses(qtd_meses_1, qtd_meses_2):
    soma_meses = qtd_meses_1 + qtd_meses_2
    return soma_meses

def crescimento_percentual_fatura(valor_fatura, saldo_devedor):
    aumento_percentual = ((valor_fatura - saldo_devedor) /saldo_devedor) * 100
    return aumento_percentual

principal()