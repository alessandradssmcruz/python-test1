frutas = ["laranja", "maçã", "banana", "uva"]
print(frutas)
print(frutas[0])
print(frutas[1])

frutas = []
print(frutas)

letras = list("suzy")
print(letras)

numeros = list(range(7))
print(numeros)

carros = ["Fusca", "Civic", 420000000, 2020, 2900, "Onix", True]
print(carros)

lista = ["p", "y", "t", "h", "o", "n"]
print(lista[2:])
print(lista[2:4])
print(lista[:3])
print(lista[2:5])
print(lista[2:5:2])
print(lista[::])
print(lista[::-1])  # Inverte a lista

carros = ["gol", "civic", "ferrari", "fusca"]
for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(indice, carro)

numeros = [1, 2, 3, 4, 5]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)
# Listas são mutáveis

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
meses_com_m = []

for mes in meses:
    if mes.startswith("m"):
        meses_com_m.append(mes)
print(meses_com_m)

numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares2 = [numero for numero in numeros2 if numero % 2 == 0]
print(pares2)

numeros3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = [numero ** 2 for numero in numeros3]
print(quadrado)