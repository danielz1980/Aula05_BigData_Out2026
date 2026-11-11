valor_pedido = float(input("Digite o valor do pedido (R$): "))
distancia = float(input("Digite a distância (Km): "))

if distancia <= 3 and valor_pedido > 50:
    frete = 0
    print("Entrega gratuita!")
else:
    frete = 8
    print(f"Incluída taxa de entrega de R$ {frete:.2f}")

valor_total = valor_pedido + frete
print(f"Valor total do pedido: R$ {valor_total:.2f}")
