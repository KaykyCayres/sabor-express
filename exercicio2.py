num = int(input("Digite um numero inteiro: "))

if num % 2 == 0:
    print(f"{num} é par!")
else:
    print(f"{num} é impar!")

idade = int(input("Qual a sua idade? "))

if idade <= 12:
    print("Voce é criança")
elif 13 <= idade < 18:
    print("Voce é adolescente")
elif idade >= 18:
    print("Voce é adulto")
else:
    print("Invalido")

usuario_certo = "Kayky"
senha_certa = "12345"

usuario_digitado = input("Digite o nome de usuario: ")
senha_digitada = input("Digite a senha: ")

if usuario_digitado == usuario_certo and senha_digitada == senha_certa:
    print("Acesso liberado")
else:
    print("Acesso negado")

coordenada_x = int(input("Digite a coordenada x: "))
coordenada_y = int(input("Digite a coordenada y: "))

if coordenada_x > 0 and coordenada_y > 0:
    print("Essa coordenada esta no primeiro quadrante do plano cartesiano")
elif coordenada_x < 0 and coordenada_y > 0:
    print("Essa coordenada esta no segundo quadrante do plano cartesiano")
elif coordenada_x < 0 and coordenada_y < 0:
    print("Essa coordenada esta no terceiro quadrante do plano cartesiano")
elif coordenada_x > 0 and coordenada_y < 0:
    print("Essa coordenada esta no quarto quadrante do plano cartesiano")
else:
    print("A coordenada está localizada no eixo ou origem")