opcao = int(input("Informe a opção desejada:\n1 - Saque\n2 - Extrato\n"))
if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
    saldo = 1000
    if valor <= saldo:
        print("Saldo disponível")
        print("Retire seu dinheiro na boca do caixa")
    else:
        print("Saldo insuficiente")
        print("Tente um valor menor ou consulte o gerente")
elif opcao == 2:
    print("Exibindo extrato...")