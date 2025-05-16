
import matplotlib.pyplot as plt

preferencias = {
    'Android': 200,
    'iOS': 100
}
plt.bar(preferencias.keys(), preferencias.values())
plt.title('Preferência de Sistema Operacional')
plt.xlabel('Sistema Operacional')
plt.ylabel('Número de Pessoas')
plt.show()

print("\nResultados:")
for sistema, votos in preferencias.items():
    print(f"{sistema}: {votos} votos")

total_votos = sum(preferencias.values())
for sistema, votos in preferencias.items():
    porcentagem = (votos / total_votos) * 100
    print(f"{sistema}: {porcentagem:.2f}%")