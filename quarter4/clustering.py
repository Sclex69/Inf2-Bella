import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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
).dropna()

# 3. Generate the Clustermap
sns.clustermap(
    result,
    cmap='viridis',
    figsize=(12, 10),
    method='ward',
    standard_scale=1
)
plt.show()

# 4. K-Means
# First: Initialize
kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto")

# Second: FIT (Must happen before you can print labels!)
kmeans.fit(result)

# Third: Now it's safe to print and predict
print("Labels:", kmeans.labels_)
print("Centers:", kmeans.cluster_centers_)
print("Prediction:", kmeans.predict([[0, 0, 0], [12, 3, 20]]))

# 5. Add labels back and plot
result['Cluster'] = kmeans.labels_

sns.pairplot(result, hue='Cluster', palette='viridis')
plt.show()