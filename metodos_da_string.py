nome = "suzy"
nome_completo = "suzy cruz"
nome2 = "    Suzy "
nome3 = "Suzy Cruz"

print(nome.upper())  # Converte para maiúsculas
print(nome3.lower())  # Converte para minúsculas
print(nome.title())  # Converte para título (primeira letra maiúscula de cada palavra)
print(nome_completo.capitalize())  # Converte a primeira letra para maiúscula
print(nome_completo.title()) # 
print(nome2.strip())  # Remove espaços em branco no início e no final
print(nome2)
print(nome2.lstrip())  # Remove espaços em branco no início
print(nome2.rstrip())  # Remove espaços em branco no final
print(nome2.replace("Suzy", "Ana"))  # Substitui "Suzy" por "Ana"
print(nome2.split())  # Divide a string em uma lista de palavras
print(nome.center(20, "*"))  # Centraliza a string em um campo de 20 caracteres, preenchendo com "*"
print(".".join(nome))  # Junta os caracteres da string com "."
print(nome.center(12, "s")) 
print("letras separadas: " + "-".join(nome))  # Junta os caracteres da string com "-"