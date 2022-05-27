convidados = input('Quantos convidados tera a festa?')
lista_de_convidados = []
i=1

while i <= int(convidados) :
    nomes=input('Informe o nome do convidado #'+ str(i) +': ')
    lista_de_convidados.append(nomes)
    i= i +1

for convidado in lista_de_convidados:
    print(convidado)

