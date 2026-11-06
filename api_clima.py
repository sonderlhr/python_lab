import requests

cidade = input("Digite uma cidade: ")

url =f"https://wttr.in/{cidade}?format=j1"

resposta = requests.get(url)

dados = resposta.json()

temperatura = dados["current_condition"][0]["temp_C"]

print(f"A temperatura em {cidade} é {temperatura}°C")