import requests

apikey = "9E505DFA-F191-4C40-A63B-7F8E2CCFF9AB"
url = "https://rest.coinapi.io/v1/exchangerate/{}/{}"

cabecera = {"X-CoinAPI-Key": apikey}

seguir = 's'
while seguir == 's':
    de = input("Moneda de origen: ")
    a = input("Moneda de destino: ")
    respuesta = requests.get(url.format(de, a), headers=cabecera)

    if respuesta.status_code == 200:
        print(respuesta.json()["rate"])
    else:
        print(respuesta.status_code)
        print(respuesta.json())

    seguir = input("Quieres más (S/N): ").lower()


