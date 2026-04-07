import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("filtrovanie_maraton.csv")

# 1. Helper function for time conversion
def time_to_hours(t_str):
    try:
        if t_str == '---' or pd.isna(t_str): return None
        h, m, s = map(int, str(t_str).split(':'))
        return h + m/60 + s/3600
    except: return None

# 2. Prepare all intermediate time columns
time_cols = ['10 km', '21,1 km', '31,1 km', 'Čas']
for col in time_cols:
    df[col + '_h'] = df[col].apply(time_to_hours)

# 3. Identify "Ondro" (SZÉKELY) for the comparison
ondro_res = df[df['Priezvisko'] == 'SZÉKELY']
ondro_time = ondro_res['Čas_h'].values[0] if not ondro_res.empty else None

# --- DIAGRAM 1: Box Plot & Violin Plot (Total Time) ---
plt.figure(figsize=(12, 6))
# Create Violin plot first
sns.violinplot(x='Kategórie', y='Čas_h', data=df, inner=None, color=".8")
# Overlay Box plot
sns.boxplot(x='Kategórie', y='Čas_h', data=df, width=0.2, boxprops={'zorder': 2})

plt.title('Comparison of Total Time Distribution by Category', fontsize=14)
plt.xlabel('Runner Category', fontsize=12)
plt.ylabel('Time (Hours)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(['Violin (Density)', 'Box (Quartiles)'], loc='upper right')
plt.tight_layout()

# --- DIAGRAM 2: KDE Plot with Ondro Position ---
plt.figure(figsize=(12, 6))
sns.kdeplot(data=df, x='Čas_h', hue='Kategórie', fill=True, common_norm=False, alpha=0.4)

if ondro_time:
    plt.axvline(ondro_time, color='red', linestyle='--', linewidth=2, label=f'Ondro Time: {ondro_time:.2f}h')

plt.title('KDE Plot: Data Distribution of Time for Each Category', fontsize=14)
plt.xlabel('Time (Hours)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend(title='Category / Highlight', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# --- DIAGRAM 3: Intermediate Times (Scatter + Lineplot) ---
# Compute mean for each category for 10km, 21.1km, 31.1km, and Final Time
inter_h_cols = [c + '_h' for c in time_cols]
mean_progress = df.groupby('Kategórie')[inter_h_cols].mean().T

plt.figure(figsize=(12, 6))
# Plotting the mean progress as connected dots
for category in mean_progress.columns:
    plt.plot(mean_progress.index, mean_progress[category], marker='o', label=category)

plt.title('Mean Pace Development Across Race Checkpoints', fontsize=14)
plt.xlabel('Race Milestone (Intermediate Times)', fontsize=12)
plt.ylabel('Average Time (Hours)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()