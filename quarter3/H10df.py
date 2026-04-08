import pandas as pd
import numpy as np

# 1. Create the dataset using NumPy
# This generates a 20x3 array of random integers between 1 and 6
data = np.random.randint(1, 7, size=(20, 3))

# 2. Create DataFrame
df = pd.DataFrame(data, columns=['kocka1', 'kocka2', 'kocka3'])

# 3. Add calculated columns
df['sum'] = df['kocka1'] + df['kocka2'] + df['kocka3']
df['sucin'] = df['kocka1'] * df['kocka2']

# This provides mean, min, max, etc., for all columns
print("--- DataFrame Statistics ---")
print(df.describe())


# Filtering
print("\n--- Rows where sum > 10 ---")
print(df[df['sum'] > 10])

print("\n--- Full DataFrame ---")
print(df)