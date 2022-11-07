print('Assinatura Cliente')
tipo_cliente = input('Informe o tipo de Cliente: Basic, Silver, Gold, Platinum:')
anual = float(input('Insira o valor do faturamento: '))

if tipo_cliente.upper() == 'BASIC':
    print(f'Valor que deve ser pago pelo cliente Basic é de {anual * 30 / 100}')
elif tipo_cliente.upper() == 'SILVER':
    print(f'Valor que deve ser pago pelo cliente Silver é de {anual * 20 / 100}')
elif tipo_cliente.upper() == 'GOLD':
    print(f'Valor que deve ser pago pelo cliente Gold é de {anual * 10 / 100}')
elif tipo_cliente.upper() == 'PLATINUM':
    print(f'Valor que deve ser pago pelo cliente Platinum é de {anual * 5 / 100}')
else:
    print('Cliente Inexistente')
