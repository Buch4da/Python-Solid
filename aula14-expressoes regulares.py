import re
import requests

requisicao = requests.get("https://www.mercadolivre.com.br")


padrao = re.findall(r'[\w\.\_-]+@[\w\.\_-]+\.[\w\.-]+',requisicao.text)

if padrao:
    print(padrao)
else:
    print("padrao nao encontrado")