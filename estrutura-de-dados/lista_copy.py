lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()  # Faz uma cópia rasa da lista
print(l2)
print(lista)
print(id(lista), id(l2))

numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(numeros)