saque = int(input("Digite o valor do saque: "))
saldo = 1000

status = "Sucesso" if saque <= saldo else "Falha"
print(f"{status} ao realizar o saque")