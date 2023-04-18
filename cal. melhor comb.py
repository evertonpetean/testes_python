while True:
    print('\nVerificar melhor opção de combustivel.\n')    
    try:
        c1 = float(input('Qual o preço do Etanol? ').replace(',', '.'))
        c2 = float(input('Qual o preço da Gasolina? ').replace(',', '.'))
        if c1 <= 0 or c2 <= 0:
            raise ValueError('Os preços dos combustíveis devem ser números positivos.')
        r = round(c1/c2, 1)
        if r >= 0.7:
            print('\nR =', r, '\nCompensa abastecer com gasolina!')
        else:
            print('\nR =', r, '\nCompensa abastecer com etanol!')
        resposta = int(input('\n1-Calcular novamente.\n2-Sair.\nDigite a opção desejada: '))
        if resposta != 1:
            print('FIM!')
            break
    except ValueError as e:
        print('Erro:', e)
    

    

    







