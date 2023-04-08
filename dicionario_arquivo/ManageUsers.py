from dicionario_arquivo.Funcoes import *
usuarios={}
opcao=perguntar()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L" :
    #inserir novos usuarios para um novo dicionario de dados
    if opcao=="I":
        inserir(usuarios)
        opcao = perguntar()
    # listar todos os usuarios dicionario de dados
    if opcao == "L":
        listar(usuarios)
        opcao = perguntar()


else:
        print("script parou, clique em executar ativar o script")
