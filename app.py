import pandas as pd
import matplotlib.pyplot as plt
import upsetplot as ups

data = pd.read_csv("motivos.csv")

motivos_unicos = set()
for lista in data['motivos']:
    motivos_unicos.update(lista)
motivos_unicos = sorted(list(motivos_unicos))

for motivo in motivos_unicos:
    data[motivo] = data['motivos'].apply(lambda x: motivo in x)

# Agrupar os dados e contar as ocorrências
grouped = data.groupby(list(motivos_unicos)).size().reset_index(name='count')

# Criar o MultiIndex
df_upset = grouped.set_index(list(motivos_unicos))

ups.UpSet(
    df_upset['count'], 
    # min_subset_size=12, 
    show_counts=True,
).plot()

plt.savefig('/app_data/motivos.png', format='png')
print("Imagem salva em /app_data/motivos.png")