numero = float(input("Digite um número: "))

match numero:
    case 0:
        print("Você digitou zero")
    case numero if 0 < numero:
        print("Você digitou um número positivo")
    case numero if numero < 0:
        print("Você digitou um número negativo")