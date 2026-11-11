# Estrutura Match Case

print ('''
[1] - Sul
[2] - Norte
[3] - Leste
[4] - Oeste
[5 ou 6] - Nordeste
[7, 8 ou 9] - Sudeste
[10] - Centro-Oeste
[11] - Noroeste
''')

codigo_origem = int(input("Informe o código de origem: "))
print()

match codigo_origem:
    case 1:
        print("Região de procedência: Sul")
    case 2:
        print("Região de procedência: Norte")
    case 3:
        print("Região de procedência: Leste")
    case 4:
        print("Região de procedência: Oeste")
    case 5 | 6:
        print("Região de procedência: Nordeste")
    case 7 | 8 | 9:
        print("Região de procedência: Sudeste")
    case 10:
        print("Região de procedência: Centro-Oeste")
    case 11:
        print("Região de procedência: Noroeste")
    case _:
        print("Produto importado")