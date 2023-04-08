import json

dicionario = {"CHAVES":["CHAVES DAS 8", "14/01/12", "RECEP_01"],
"QUICO":["QUICO DAS 8", "14/01/12", "RECEP_02"],
"FLORINDA":["FLORINDA DAS 8", "14/01/12", "RECEP_04"]  }

#criando um arquivo json atraves do script python
#with open("bd1.json", "w") as json_file:
  #  json.dump(dicionario,json_file)

#lendo o arquivo json
with open("bd1.json", "r") as json_file:
    dicionario = json.load(json_file)
    for chave, dados in dicionario.items():
        print(chave + " : " + str(dados))
