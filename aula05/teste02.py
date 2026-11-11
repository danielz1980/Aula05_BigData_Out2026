# alias = ["nome", "idade", "altura", "peso"]
# aluno1 = ["Daniel", 30, 1.75, 70]

# catalogo = dict(zip(alias, aluno1))

# print(catalogo)

# catalogo.update({"idade": 31, "peso": 72})
# print(catalogo)

dicionario = {"nome": "Daniel", "idade": 30, "altura": 1.75, "peso": 70}

# Iterando pelas chaves
for chave in dicionario.keys():
    print(chave)

# Iterando pelos valores
for valor in dicionario.values():
    print(valor)

# Iterando por chaves e valores
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")