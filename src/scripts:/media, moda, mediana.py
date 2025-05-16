

import json
from statistics import mean, median, mode

with open('cadastros.json','r') as file:
    dados = json.load(file)
    print(dados)

idades = [item['idade'] for item in dados]

media_idade = mean(idades)
mediana_idade = median(idades)
moda_idade = mode(idades)

print(f'Média das idades: {media_idade}')
print(f'Mediana das idades: {mediana_idade}')
print(f'Moda das idades: {moda_idade}')
