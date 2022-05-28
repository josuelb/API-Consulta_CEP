import requests

print("""
####################
### Consulta CEP ###
####################
""")

cep_user = input("Digite o CEP para a consulta: ")

if len(cep_user) != 8:
    print('Quantidade de dígitos inválida')
    exit()

#https://viacep.com.br/ws/01001000/json/


request = requests.get(f'https://viacep.com.br/ws/{cep_user}/json/')
addres_data = request.json()

if 'erro' in addres_data:
    print('Desculpa, CEP invalido')
else:
    print(addres_data)