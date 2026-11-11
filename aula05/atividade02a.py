valor_pedido = float(input("Digite o valor do pedido (R$): "))
distancia = float(input("Digite a distância (Km): "))
frete = 8

if distancia <= 3 and valor_pedido > 50:
    print(f"Valor total do pedido: R$ {valor_pedido:.2f}")
    print("Entrega gratuita!")
else:
    valor_total = valor_pedido + frete
    print(f"Valor total do pedido: R$ {valor_total:.2f}")
    print(f"Incluído taxa de entrega de R$ {frete:.2f}")