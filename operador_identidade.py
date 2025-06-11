curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(nome_curso is curso)  # True, nome_curso é o mesmo objeto que curso
print(nome_curso is not curso)  # False, nome_curso é o mesmo objeto que curso
print(saldo is limite)  # True, saldo e limite ocupam a mesma posição na memória 
print(saldo is not limite)  # False, saldo e limite ocupam a mesma posição na memória 

saldo = 300
limite = 300
print(saldo is limite)  # TRUE, ocupam a mesma posição na memória 
print(saldo is not limite)  # FALSE

saldo = 300
limite = 400
print(saldo is limite) 
print(saldo is not limite)