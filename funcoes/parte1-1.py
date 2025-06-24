def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([1, 2, 3, 4, 5]))  # Exemplo de uso da função calcular_total
print(retornar_antecessor_e_sucessor(10))