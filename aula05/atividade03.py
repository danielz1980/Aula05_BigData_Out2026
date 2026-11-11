valor_compra = float(input("Digite o valor da compra (R$): "))
cliente_cadastrado = input("O cliente está cadastrado? (S/N): ")
frete = 25.00

if valor_compra > 200 or cliente_cadastrado.upper()[0] == "S":
    mensagem = 'Cliente tem direito a frete grátis.'
    valor_final = valor_compra
else:
    mensagem = f'Cliente não tem direito a frete grátis. Incluído frete de R$ {frete:.2f}'
    valor_final = valor_compra + frete

print(mensagem)
print(f"Valor final: R$ {valor_final:.2f}")