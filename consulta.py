import requests

apikey = "9E505DFA-F191-4C40-A63B-7F8E2CCFF9AB"
url = "https://rest.coinapi.io/v1/exchangerate/BTC/EUR"

cabecera = {"X-CoinAPI-Key": apikey}
respuesta = requests.get(url, headers=cabecera)

print(respuesta.status_code)
midiccionario = respuesta.json()
print(midiccionario['rate'])

print(respuesta.json()["rate"])
    
