n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4
print(f"A média das notas é: {media:.2f}")

if media >= 7:
    print("Aluno aprovado!")
elif media >= 5:
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado!")