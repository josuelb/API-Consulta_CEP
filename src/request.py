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

# https://viacep.com.br/ws/01001000/json/


request = requests.get(f'https://viacep.com.br/ws/{cep_user}/json/')
addres_data = request.json()

if 'erro' in addres_data:
    print('Desculpa, CEP invalido')
else:
    db = f"""
    CEP: {addres_data['cep']},
    Logradouro: {addres_data['logradouro']},
    Complemento: {addres_data['complemento']},
    Bairro: {addres_data['bairro']},
    Localidade: {addres_data['localidade']}, UF: {addres_data['uf']},
    IBGE: {addres_data['ibge']},
    GIA: {addres_data['gia']},
    DDD: {addres_data['ddd']},
    SIAFI: {addres_data['siafi']}
    """
