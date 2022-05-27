import requests   #Beautiful Soup 4 BS4

cabecalho = {'User agent': 'Windows 12',
             'Referer': 'https://google.com'}
meus_cokies = {'Ultima-visita': '10-10-2020'}

dados = {'username': 'Buchada',
         'password': '123'}

try:
    requisicao = requests.post('https://putsreq.com/jtow0Y3YI4hFZa4LsOok',
                               headers=cabecalho,
                               cookies=meus_cokies,
                               data=dados)
    texto = requisicao.text
except Exception as e:
    print("Requisicao de erro:", e)

print(texto)