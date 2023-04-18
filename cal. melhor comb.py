cont=1
while cont==1:
    print('\nVerificar melhor opção de combustivel.\n')    
    c1=float(input('Qual o preço do Etanol? '))
    c2=float(input('Qual o preço da Gasolina? ')) 
    r=round(c1/c2,1)
    if r>=0.7:
        print('\nR=',(r),'\nCompensa abastecer com gasolina!')
    else:
        print('\nR=',(r),'\nCompensa abastecer com etanol!')
    resposta=int(input('\n1-Calcular novamente.\n2-Sair.\nDigite a opção desejada: '))
    if resposta!=1:
        cont+=1
        print('FIM!')    
    

    

    







