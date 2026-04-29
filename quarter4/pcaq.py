import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Load and clean data
df = pd.read_excel('UN data.xlsx', sheet_name='Population, Surface Area and De', skiprows=1)
target_series = [
    'Population mid-year estimates (millions)',
    'Population density',
    'Population aged 60+ years old (percentage)'
]

filtered_df = df[df['Series'].isin(target_series)].copy()
filtered_df['Value'] = pd.to_numeric(filtered_df['Value'], errors='coerce')

# 2. Pivot the table
result = filtered_df.pivot_table(
    index=['Region/Country/Area name', 'Year'],
    columns='Series',
    values='Value'
).reset_index().dropna()

# 3. Scaling and PCA
features = target_series
x = result[features].values
x_scaled = StandardScaler().fit_transform(x)

# FIX: components=2 means the result has two columns
pca = PCA(n_components=2)
pca_components = pca.fit_transform(x_scaled)

# Assign both components to the dataframe
result['PCA_1'] = pca_components[:, 0]
result['PCA_2'] = pca_components[:, 1]

# 4. Visualization
plt.figure(figsize=(10, 6))
# Using both components for a 2D scatter plot
plt.scatter(result['PCA_1'], result['PCA_2'], alpha=0.5, color='purple', s=15)

plt.title('PCA of UN Population Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

