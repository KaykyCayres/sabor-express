import os

restaurantes = [{"nome":"Sushi Mania", "categoria":"Japonesa", "ativo":False}, {"nome":"Pizza Italy", "categoria":"Italiana", "ativo":False}, {"nome":"Al Libha", "categoria":"Arabe", "ativo":True}]

def exibir_nome():
    """Exibe o nome do programa"""
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    """Exibe todas as opcoes possiveis do programa"""
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar/Desativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    """Exibe apenas o texto na hora de finalizar o app"""
    exibir_subtitulo("Finalizando app")

def voltar_menu_principal():
    """Volta ao menu quando digitar uma tecla"""
    input("\nDigite uma tecla para voltar ao menu ")
    main()

def exibir_subtitulo(texto):
    """Exibe os subtitulos de cada opcao do aplicativo"""
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    """Exibe um texto de opcao invalida quando necessario"""
    print("Opcao invalida!\n")
    voltar_menu_principal()

def cadastrar_restaurante():
    """Cadrastro de novos restaurantes ao programa"""
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_restaurante = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
    dados_restaurante = {"nome":nome_restaurante, "categoria":categoria_restaurante, "ativo":False}
    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado!")
    voltar_menu_principal()

def listar_restaurantes():
    """Lista os restaurantes ja cadastrados no programa"""
    exibir_subtitulo("Listando todos os restaurantes")
    print(f"{"Nome".ljust(22)} | {"Categoria".ljust(22)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo_restaurante = "ativado" if restaurante["ativo"] else "desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}")
    voltar_menu_principal()

def ativar_desativar_restaurante():
    """Ativa ou desativa os restaurantes cadastrados no programa"""
    exibir_subtitulo("Ativar/Desativar restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print(f"O restaurante {nome_restaurante} nao foi encontrado")
    voltar_menu_principal()

def escolher_opcoes():
    """Escolha do usuario para opcao que deseja prosseguir"""
    try:
        opcao_escolhida = int(input("Escolha uma opcao: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_desativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida

def main():
    """Define o que o programa deve fazer quando iniciar"""
    os.system("cls")
    exibir_nome()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
    main()