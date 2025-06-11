curso = "Curso de Python"
frutas = ["maçã", "banana", "laranja"]
saques = [100, 200, 300]

print("Python" in curso)  # True, "Python" está contido em curso
print("python" in curso)  # False, "python" não está contido em curso
print("uva" in frutas)  # False, "uva" não está na lista de frutas
print("maçã" not in frutas)  # False, "maçã" está na lista de frutas
print(100 in saques)  # True, 100 está na lista de saques