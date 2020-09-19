# Fazendo operacões com set
# União
# Interseção
# Diferença
# Diferença Simetrica
# Criando os conjuntos
conjunto_A = set([1, 2, 3])
conjunto_B = set([3, 4, 5])
print('conjunto A:', conjunto_A)
print('conjunto B:', conjunto_B)

# União
uniao = conjunto_A.union(conjunto_B)
print('União A & B:', uniao) # Ou seja não repetiu o 3

# Interseção
intersecao = conjunto_A.intersection(conjunto_B)
print('Interseção A & B:', intersecao)

# Diferença
diferenca = conjunto_A.difference(conjunto_B)
print('Diferença A - B:', diferenca)

# Difrença simetrica
diferenca_simetrica = conjunto_A.symmetric_difference(conjunto_B)
print('Dirença simetrica entre A e B:', diferenca_simetrica)