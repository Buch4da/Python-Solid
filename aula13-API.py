import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=cf8413be&t=' + titulo +'&type=movie')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print("Erro na conexao")
        exit()

def printar_detalhes(filme):
    print("Titulo:", filme["Title"])
    print("Ano:", filme["Year"])
    print("Diretor:", filme["Director"])
    print("Atores:", filme["Actors"])
    print("Nota:", filme["imdbRating"])
    print("Premios:", filme["Awards"])
    print("Poster:", filme["Poster"])
    print("")

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar')

    if op == 'SAIR':
        sair = True
        print("saindo...")
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print("Filme nao encontrado")
        else:
            printar_detalhes(filme)