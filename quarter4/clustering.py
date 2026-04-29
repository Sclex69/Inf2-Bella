import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
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
# We set the index here so that these columns aren't treated as data for clustering
result = filtered_df.pivot_table(
    index=['Region/Country/Area name', 'Year'],
    columns='Series',
    values='Value'
).dropna()
print(result)




# 4. Generate the Clustermap
# If you have hundreds of rows, you might want to sample the data first: df_scaled.sample(50)
g = sns.clustermap(
    result,
    cmap='viridis',
    figsize=(12, 10),
    method='ward',
    standard_scale=1
)

plt.show()

print(result)

#create k-means model
kmeans = KMeans(n_clusters = 2, random_state = 0, n_init = "k-means++")
kmeans.fit(result)

print(kmeans.labels_)
print(kmeans.predict([[0, 0], [12, 3]]))
print(kmeans.cluster_centers_)