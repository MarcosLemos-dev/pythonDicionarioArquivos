from dicionario_arquivo.Funcoes import *
usuarios={}
opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L" :
    if opcao=="I":
        inserir(usuarios)
        opcao = perguntar()

    if opcao == "L":
        listar(usuarios)
        opcao = perguntar()
else:
        print("script parou, clique em executar ativar o script")