saldo = 1000
saque = float(input("Digite o valor do saque: "))
if saque <= saldo:
    print("Saldo disponível")
    print("Retire seu dinheiro na boca do caixa")
else:
    print("Saldo insuficiente")