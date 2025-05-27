import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ler o arquivo CSV
df = pd.read_csv(
    r'C:\Users\trend\Desktop\programação\ecommerce_preparados.csv')

# Garantir que a coluna 'Preço_MinMax' seja numérica
df['Preço_MinMax'] = pd.to_numeric(df['Preço_MinMax'], errors='coerce')

# Estilo visual dos gráficos
sns.set(style="whitegrid")

# 1. Histograma - Notas
plt.figure(figsize=(8, 5))
sns.histplot(df['Nota'], bins=10, kde=True)
plt.title('Distribuição das Notas dos Produtos')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

# 2. Gráfico de Dispersão - Nota x Avaliações
plt.figure(figsize=(8, 5))
sns.scatterplot(x='N_Avaliações', y='Nota', data=df)
plt.title('Dispersão: Número de Avaliações vs Nota')
plt.xlabel('Número de Avaliações')
plt.ylabel('Nota')
plt.tight_layout()
plt.show()

# 3. Mapa de Calor das Correlações
plt.figure(figsize=(10, 8))
correlation = df[['Nota', 'N_Avaliações', 'Desconto', 'Nota_MinMax',
                  'N_Avaliações_MinMax', 'Preço_MinMax']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor das Correlações')
plt.tight_layout()
plt.show()

# 4. Gráfico de Barras - Marcas mais frequentes
top_marcas = df['Marca'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_marcas.values, y=top_marcas.index)
plt.title('Top 10 Marcas Mais Frequentes')
plt.xlabel('Frequência')
plt.ylabel('Marca')
plt.tight_layout()
plt.show()

# 5. Gráfico de Pizza - Gênero
genero_counts = df['Gênero'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(genero_counts, labels=genero_counts.index,
        autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Gênero dos Produtos')
plt.tight_layout()
plt.show()

# 6. Gráfico de Densidade - Preço
plt.figure(figsize=(8, 5))
sns.kdeplot(x=df['Preço_MinMax'].dropna(), fill=False)
plt.title('Densidade do Preço Normalizado dos Produtos')
plt.xlabel('Preço Normalizado')
plt.ylabel('Densidade')
plt.tight_layout()
plt.show()

# 7. Gráfico de Regressão - Desconto x Nota
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x='Desconto', y='Nota', scatter_kws={"alpha": 0.5})
plt.title('Relação entre Desconto (%) e Nota do Produto')
plt.xlabel('Desconto (%)')
plt.ylabel('Nota')
plt.tight_layout()
plt.show()
