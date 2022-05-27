from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 6, 'ford', 10)

print("Caminhao Rosa")
print("Cor:",caminhao_rosa.cor )
print("Marca:",caminhao_rosa.marca)
print("Tanque:",caminhao_rosa.tanque)

print("")
carro_azul = Carro('Azul', "Fiat", 30)

print("Carro Azul")
print("Cor:",carro_azul.cor )
print("Marca:",carro_azul.marca)
print("Tanque:",carro_azul.tanque)
carro_azul.abastecer(30)
print("Tanque:",carro_azul.tanque)