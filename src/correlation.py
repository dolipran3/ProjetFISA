import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
df = pd.read_csv('data/df_venues_processed.csv', sep=';')

# Sélectionner les colonnes numériques
numeric_cols = df.select_dtypes(include=[np.number]).columns

# Calculer la matrice de corrélation (Pearson par défaut)
correlation_matrix = df[numeric_cols].corr()

# Autres méthodes possibles :
# correlation_matrix = df[numeric_cols].corr(method='spearman')
# correlation_matrix = df[numeric_cols].corr(method='kendall')

# Heatmap de la matrice de corrélation
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', 
            center=0, fmt='.2f', linewidths=0.5)
plt.title('Matrice de corrélation')
plt.tight_layout()
plt.show()

# Trouver les corrélations les plus fortes avec une variable cible
target = 'Total_reservations'
correlations = correlation_matrix[target].sort_values(ascending=False)
print(correlations)

# Filtrer les corrélations significatives
strong_corr = correlation_matrix[abs(correlation_matrix) > 0.5]