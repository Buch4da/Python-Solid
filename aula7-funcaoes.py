def maior (n1):
    maior_item = n1[0]
    for i in n1:
        if i > maior_item :
            maior_item = i
    return maior_item

def menor (n1):
    menor_item = n1[0]
    for i in n1:
        if i < menor_item :
            menor_item = i
    return menor_item

def temsete(argumento):
    if len(argumento) == 7:
        return True
    else :
        return False


print(maior([1,2,3,4,5,6,7,8]))
print(menor([1,2,3,4,5,6,7,-4]))

#if temsete ([1,2,3,4,5,6,7]):
 #   print("tem sete letras")
#else:
 #   print('nao tem')
