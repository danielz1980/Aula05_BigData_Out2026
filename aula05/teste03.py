nome = input("Informe seu nome: ").lower()

match nome:
    case "alice":
        print("Olá, Alice!")
    case "bob":
        print("Olá, Bob!")
    case _:
        print("Olá, desconhecido!")