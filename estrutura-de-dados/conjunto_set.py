numeros = set([1,1,2,3,4,5,5])
print(numeros)  # {1, 2, 3, 4, 5}

print(type(numeros))  # <class 'set'>


letras = set("abacaxi")
print(letras)  #  {'a', 'b', 'c', 'i', 'x'}

carros = set(["Fusca", "Civic", "Civic", "Civic", "Civic", "Civic"])
print(carros)  # {'Fusca', 'Civic'}

linguagens = set(["Python", "Java", "C", "C++", "JavaScript"])
print(linguagens)  # {'C', 'Java', 'C++', 'JavaScript', 'Python'}

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

# União
uniao = conjunto_a | conjunto_b # ou conjunto_a.union(conjunto_b)   
print(uniao)  # {1, 2, 3, 4, 5, 6, 7, 8}
# Interseção
intersecao = conjunto_a & conjunto_b # ou conjunto_a.intersection(conjunto_b)
print(intersecao)  # {4, 5}

# Diferença
diferenca = conjunto_a - conjunto_b  # ou conjunto_a.difference(conjunto_b)
print(diferenca)  # {1, 2, 3}   

# Diferença Simétrica
diferenca_simetrica = conjunto_a ^ conjunto_b  # ou conjunto_a.symmetric_difference(conjunto_b)
print(diferenca_simetrica)  # {1, 2, 3, 6, 7, 8}

# Verifica se um elemento está no conjunto
print(1 in conjunto_a)  # True  

# exemplo do issubset
conjunto_c = {1, 2, 3}
print(conjunto_c.issubset(conjunto_a))  # True
print(conjunto_c.issubset(conjunto_b))  # False

# exemplo do issuperset 
print(conjunto_a.issuperset(conjunto_c))  # True
print(conjunto_b.issuperset(conjunto_c))  # False

# exemplo do isdisjoint
conjunto_d = {6, 7, 8}
print(conjunto_a.isdisjoint(conjunto_d))  # True
print(conjunto_b.isdisjoint(conjunto_d))  # False