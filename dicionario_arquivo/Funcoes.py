from builtins import str


def perguntar():
    resposta = input("O que deseja realizar? \n"
                    + "<I> - Para Inserir um dicionario\n"
                     + "<P> - Para Pesquisar um dicionario\n"
                   +  "<E> - Para Excluir um dicionario\n"
                +  "<L> - Para Listar todos dicionario: \n"
                     +  "<SAIR> - Para SAIR do script\n").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                          input("Digite a última data de acesso: "),
                                          input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)


def salvar(dicionario):
    with open("bd.txt","a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))

def listar(dicionario):
    with open("bd.txt", "r") as arquivo:
        conteudo=arquivo.readlines()
        print("Tipo de dado da variável",type(conteudo))
        print(" Conteúdo do arquivo:",conteudo)