def criar_carro(marca, modelo, ano, /, placa, motor, combustivel):
    print(marca, modelo, ano, placa, motor, combustivel)

    criar_carro("Fiat", "Uno", 2020, placa = "ABC-1234", motor = "1.0", combustivel= "Flex")  # Exemplo de uso da função criar_carro