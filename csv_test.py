
# Codigo simples para ler e filtrar csv
import pandas as pd

df = pd.read_csv('./exemplo.csv')

df_filtrado = df[df['estado'] == 'PR']

print(df_filtrado)