opcao = -1

while opcao != 0:
    opcao = int(input("Digite sua opção: \n[1] Sacar \n[2] Extrato \n[0] Sair \n"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")