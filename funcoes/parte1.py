def exibir_mensagem():
    print("Olá, mundo!")

def exibir_mensagem2(nome):
    print(f"Olá, {nome}!")

def exibir_mensagem3(nome="Antônio"):
    print(f"Olá, {nome}!")

exibir_mensagem()
exibir_mensagem2("Maria")
exibir_mensagem3()
exibir_mensagem3(nome="João")