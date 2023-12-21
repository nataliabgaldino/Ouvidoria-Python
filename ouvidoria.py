import time

reclamacao = []
rec = 0


while rec != 5:
    print('....................................................... ')   
    print('Bem vindo ao menu da Ouvidoria! ')
    print('1) para listar reclamações')
    print('2) para adicionar reclamações')
    print('3) Para remover reclamações')
    print('4) para pesquisar reclamações')
    print('5) para sair do programa')
    
    print(' ....................................................... ')
    rec = int(input('Digite aqui sua opção: '))
    time.sleep(0.5)
    
    if rec == 1 and len(reclamacao) == 0:
        for c in range(5):
            print('.')
            time.sleep(0.4)
        print('Não existem reclamações cadastradas no sistema!')
        for c in range(5):
            print('.')
            time.sleep(0.4)
    
    elif rec == 1 and len(reclamacao) > 0:
        for c in range(5):
            print('.')
            time.sleep(0.4)
        for item in range(len(reclamacao)):
            print(item+1,':', reclamacao[item])
        for c in range(5):
            print('.')
            time.sleep(0.4)
    
    elif rec == 2:
        oco = str(input('Digite aqui sua ocorrência: '))
        reclamacao.append(oco)
        for c in range(len(reclamacao)):
            print('Reclamação cadastrada com sucesso! Código', c+1, ':', reclamacao[c])
            time.sleep(0.4)
        for c in range(5):
            print('.')
            time.sleep(0.4)
    
    elif rec == 3 and len(reclamacao) > 0:
        for c in range(5):
            print('.')
            time.sleep(0.4)
        for item in range (len(reclamacao)):
            print (item +1,reclamacao[item])
        
        oco = int(input('Qual reclamação você gostaria de remover? : '))
        reclamacao.pop(oco-1)
        print('Reclamação removida com sucesso!')
        for c in range(5):
            print('.')
            time.sleep(0.4)
   
    elif rec == 3 and len(reclamacao) == 0:
        for c in range(5):
            print('.')
            time.sleep(0.4)
        print('Não existem reclamações cadastradas no sistema!!')

    elif rec == 4:
        print('Qual o Código da reclamação')
        cod = int(input('Digite o código: '))
        if 1<= cod <= len(reclamacao):
            cod2 = reclamacao[cod-1]
            print('reclamação', cod)
            print(cod2)
            for c in range(5):
                print('.')
                time.sleep (0.3)   
        else:
            print('Código Inválido, por favor tente novamente!')
            for c in range(4):
                print('.')
                time.sleep(0.3)

    elif rec == 5:
        for c in range(5):
            print('.')
            time.sleep(0.4)
        print('Obrigado por usar nossa ouvidoria! Volte sempre!!')
        
    else:
        for c in range(5):
            print('.')
            time.sleep(0.4)
        print('A opção selecionada é inválida!!!')
        print('Por favor reinicie a ouvidoria e tente novamente!')
        for c in range(5):
            print('.')
        time.sleep(0.4)