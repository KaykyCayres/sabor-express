pessoa = {"nome":"Kayky", "idade":18, "cidade":"Sao Paulo"}
print(pessoa)

pessoa["idade"] = 20
print(pessoa)

pessoa["profissao"] = "Fisioterapeuta"
print(pessoa)

del pessoa["cidade"]
print(pessoa)

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

if "nome" in pessoa:
    print("A chave existe")
else:
    print("A chave nao exite")

frase = "Hello, World!"
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)