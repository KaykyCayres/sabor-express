numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ["Kayky", "Lucas", "Felipe", "Renata"]
anos = [2008, 2026]

for numero in numeros:
    print(numero)

print()

soma_impar = 0
for i in range(1, 11, 2):
    soma_impar += i
print(soma_impar)

print()

for i in range(10, 0, -1):
    print(i)

print()

numero_tabuada = int(input("Digite um numero para tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(resultado)

print()

soma = 0
try:
    for numero in numeros:
        soma += numero
    print(soma)
except Exception as e:
    print(f"Erro: {e}")

print()

soma_valores = 0
try:
    for valor in numeros:
        soma_valores += valor
    media = soma_valores / len(numeros)
    print(media)
except ZeroDivisionError:
    print("Nao é possivel dividir por zero")
except Exception as e:
    print(f"Erro: {e}")