def sacar(valor):
    saldo = 1000
    if valor <= saldo:
        print("Saldo disponível")
        print("Retire seu dinheiro na boca do caixa")
    else:
        print("Saldo insuficiente")
        print("Tente um valor menor ou consulte o gerente")
    
    print("Obrigada por ser nosso cliente")


sacar(1500)  # Valor sacado