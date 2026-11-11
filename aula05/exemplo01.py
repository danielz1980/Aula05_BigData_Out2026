mensalidade = float(input("Digite o valor da mensalidade: "))
nota_final = float(input("Digite a nota final do aluno: "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

bolsa =  20    # 20% de desconto sobre a mensalidade

if nota_final >= 7 and frequencia >= 75:
    print(f"Bolsa de estudo concedida de {bolsa}%")
    mensalidade = mensalidade * (1 - bolsa / 100)
else:
    print("Bolsa de estudo não concedida.")

print(f"Valor da mensalidade: R$ {mensalidade:.2f}")
