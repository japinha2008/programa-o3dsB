# Lê o valor de n
n = int(input("Digite a quantidade de números: "))

# Cria a lista vazia
lista = []

# Lê n números e adiciona na lista
for i in range(n):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista.append(numero)

# Lê o valor de x
x = int(input("Digite o número a ser verificado: "))

# Verifica se x está na lista
if x in lista:
    print(f"O número {x} pertence à lista.")
else:
    print(f"O número {x} NÃO pertence à lista.")
