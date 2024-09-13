import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
df = pd.read_csv('dados.csv')

# Plotar o gráfico
plt.plot(df['x'], df['y'])

# Adicionar título e rótulos
plt.title("Gráfico de Dados do Arquivo CSV")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Exibir o gráfico
plt.show()
