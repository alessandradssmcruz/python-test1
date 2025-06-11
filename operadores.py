#soma
print(1+9)

#subtração
print(10-5)

#multiplicação
print(2*3)

#divisão
print(10/2)

#divisão inteira
print(10//3)

#resto da divisão
print(10%3)

#exponenciação
print(2**3)

#precedência de operadores
print(2 + 3 - 1)   # Adição e subtração têm a mesma precedência, são avaliados da esquerda para a direita
print(2 * 3 + 4)  # Multiplicação tem precedência sobre adição
print(2 // 3 * 4)  # Divisão inteira tem precedência sobre multiplicação
print(10 * 2 / 3)  # Multiplicação e divisão têm a mesma precedência, são avaliados da esquerda para a direita
print(10 / 2 * 3)  # Divisão e multiplicação têm a mesma precedência, são avaliados da esquerda para a direita
print(2 + 3 * 4 - 5)  # Multiplicação tem precedência sobre adição e subtração
print(2 + 3 * 4)  # Multiplicação tem precedência sobre adição  
print((2 + 3) * 4)  # Parênteses alteram a precedência
print(2 + 3 * 4 ** 2)  # Exponenciação tem precedência mais alta
# Exponenciação
print(2 ** 3 + 4)  # Exponenciação tem precedência mais alta    


# Operadores de atribuição
x = 10
x += 5  # Equivalente a x = x + 5
print(x)  # Imprime 15
# Operadores de comparação
print(5 == 5)  # Igualdade  
print(5 != 3)  # Diferença
print(5 < 10)  # Menor que
print(10 > 5)  # Maior que
print(5 <= 5)  # Menor ou igual a
print(10 >= 10)  # Maior ou igual a
# Operadores lógicos
print(True and False)  # E lógico
print(True or False)  # Ou lógico
print(not True)  # Negação lógica
# Operadores de identidade
a = [1, 2, 3]
b = a
c = a[:]
print(a is b)  # True, b é o mesmo objeto que a

print(a is c)  # False, c é uma cópia de a
print(a == c)  # True, c tem o mesmo conteúdo que a 

print(a is not c)  # True, c não é o mesmo objeto que a
print(a is not b)  # False, b é o mesmo objeto que a        

# Operadores de associação
lista = [1, 2, 3, 4, 5]
print(3 in lista)  # True, 3 está na lista
print(6 not in lista)  # True, 6 não está na lista  
# Operadores bit a bit
print(5 & 3)  # E bit a bit
print(5 | 3)  # OU bit a bit
print(5 ^ 3)  # OU exclusivo bit a bit      
print(~5)  # Negação bit a bit
print(5 << 1)  # Deslocamento à esquerda    
print(5 >> 1)  # Deslocamento à direita
# Operadores de atribuição bit a bit    
x = 5
x &= 3  # Equivalente a x = x & 3
print(x)  # Imprime 1
x = 5