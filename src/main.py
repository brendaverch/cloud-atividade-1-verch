import requests
import csv

def extrair_info_pokemon(url):
    r = requests.get(url)
    data = r.json()
    return {
        'id': data['id'],
        'nome': data['name'],
        'tipos': ','.join([t['type']['name'] for t in data['types']]),
        'altura': data['height'],
        'peso': data['weight'],
        'qtde_movimentos': len(data['moves'])
    }

with open('urls.txt') as f, open('pokemons.csv', 'w', newline='') as out:
    writer = csv.DictWriter(out, fieldnames=['id', 'nome', 'tipos', 'altura', 'peso', 'qtde_movimentos'])
    writer.writeheader()
    for url in f:
        info = extrair_info_pokemon(url.strip())
        writer.writerow(info)
