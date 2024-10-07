import requests

pokemon = input("Digite o nome do Pokémon: ").lower()
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    nome = dados["name"]
    altura = dados["height"] / 10
    peso = dados["weight"]
    print(f"Nome: {nome.capitalize()}\nAltura: {altura}\nPeso: {peso}")
else:
    print("Pokémon não encontrado. Verifique o nome e tente novamente.")