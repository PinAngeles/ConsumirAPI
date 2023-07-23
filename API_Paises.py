import requests

def lista_paises(url):
    paises = requests.get(url)
    paises = paises.json(url)

    for pais in paises:
        print(f"nombre oficial en español:{pais['translations']['spa']['official']}")
        print(f"La capital es: {pais['capital'][0]}")
        moneda = pais['currencies']
        for m in moneda.values():
            print(f"La moneda es: {m['name']}")
            print(f"Su simbolo es {m['simbolo']}")
        CodigoTelefono = pais['idd']['root'] + pais['idd']['suffixes'][0]
        print(f"El codigo de telefono es :{CodigoTelefono}")

url = 'https://restcountries.com/v3.1/independent?status=true&fields=translations,capital,currencies,idd'

lista_paises(url)