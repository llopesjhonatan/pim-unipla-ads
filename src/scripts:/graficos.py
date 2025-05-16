



import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats




data = pd.read_json('cadastros.json')

media = data['idade'].mean()
mediana = data['idade'].median()
moda = stats.mode(data['idade'])[0]


estisticas = pd.DataFrame({
    'Estatística': ['Média', 'Mediana', 'Moda'],
    'Valor': [media, mediana, moda]
    })

plt.bar(estisticas['Estatística'], estisticas['Valor'], color=['blue', 'orange', 'green'])
plt.title('Estatísticas de Idade')
plt.xlabel('Estatística')
plt.ylabel('Valor')
plt.show()
