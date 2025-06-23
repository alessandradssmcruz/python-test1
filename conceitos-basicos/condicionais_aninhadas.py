conta_normal = False
conta_universitaria = True

saldo = 1000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saldo disponível")
    elif saque <= (saldo + cheque_especial):
        print("Saldo insuficiente, mas cheque especial disponível")
    else:
        print("Saldo insuficiente, saque não realizado")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente, saque não realizado")