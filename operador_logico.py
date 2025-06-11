saldo = 1000
saque = 200
limite = 500

saldo >= saque

saque <= limite
saldo >= saque and saque <= limite  # True, pois saldo é maior ou igual a saque e saque é menor ou igual a limite
saque <= limite or saldo >= saque  # True, pois saque é menor ou igual a limite

contatos_emergencia = []

not 1000 > 5000  # True, pois 1000 não é maior que 5000
not contatos_emergencia  # True, pois a lista está vazia
not "saque 500;"    # True, pois a string não está vazia (não é avaliada como False)
not "" # True, pois a string está vazia (é avaliada como False)

saldo_suficiente = saldo >= saque
saque_valido = saque <= limite

print(saldo_suficiente and saque_valido)  # True, pois ambos são verdadeiros
print(saldo_suficiente or saque_valido)  # True, pois pelo menos um é verdadeiro

print(not saldo_suficiente)  # False, pois saldo_suficiente é True
print(not saque_valido)  # False, pois saque_valido é True  

print(saldo_suficiente)  # True, pois saldo é maior ou igual a saque
print(saque_valido)  # True, pois saque é menor ou igual a limite