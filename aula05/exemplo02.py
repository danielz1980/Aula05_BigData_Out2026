# Estrutura Match Case

print ('''
[1] - Marketing
[2] - Financeiro
[3 a 5] - Administração
[6 a 9] - TI
[10 a 20] - Serviços Gerais
''')
opcao = int(input("Escolha uma opção: "))
print()

match opcao:
    case 1:
        print("Você escolheu Marketing")
    case 2:
        print("Você escolheu Financeiro")
    case 3 | 4 | 5:
        print("Você escolheu Administração")
    case opcao if 6 <= opcao <= 9:
        print("Você escolheu TI")
    case opcao if 10 <= opcao <= 20:
        print("Você escolheu Serviços Gerais")
    case _:
        print("Opção inválida")