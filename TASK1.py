# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
import matplotlib.colors as mcolors


sns.set_theme(style="whitegrid", palette="Spectral", font_scale=1.3)
df = pd.read_csv("Mydataset.csv", sep=',')



# Extract population data for the year 2023
df['2023'] = pd.to_numeric(df['2023'], errors='coerce')
population_2023 = df['2023'].dropna()
df_2023 = df[['Country Name', '2023']].dropna()



#Create a figure with two subplots (histogram and boxplot)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [3, 1]})



# --- Histogram---
n_bins = 20
hist, bins, _ = ax1.hist(population_2023, bins=n_bins, alpha=0.8, edgecolor='black')
bin_centers = (bins[:-1] + bins[1:]) / 2

#gradient color
cmap = plt.get_cmap('Spectral')
norm = mcolors.Normalize(vmin=min(bin_centers), vmax=max(bin_centers))
colors = cmap(norm(bin_centers))
for i, patch in enumerate(ax1.patches):
    patch.set_facecolor(colors[i])

#KDE curve
sns.kdeplot(population_2023, color='red', linewidth=2, label='KDE', ax=ax1)

ax1.set_title('Distribution of Population Sizes Across Countries (2023)', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Population (in millions)', fontsize=14, fontweight='bold')
ax1.set_ylabel('Number of Countries', fontsize=14, fontweight='bold')

ax1.ticklabel_format(style='plain', axis='x')
ax1.get_xaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'{int(x/1e6)}M')
)

# Adding median
median_pop = population_2023.median()
ax1.axvline(median_pop, color='orange', linestyle='--', linewidth=2, label=f'Median: {median_pop/1e6:.1f}M')
ax1.legend(fontsize=12)

ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_facecolor('#f5f5f5')

ax1.tick_params(axis='both', labelsize=12)
for label in ax1.get_xticklabels() + ax1.get_yticklabels():
    label.set_fontweight('bold')


###
# --- Boxplot (Right Subplot) ---
sns.boxplot(y=population_2023, ax=ax2, color='lightcoral', linewidth=2, flierprops={'marker': 'o', 'color': 'red', 'markersize': 5})
ax2.set_title('Boxplot of Population Sizes', fontsize=16, fontweight='bold', pad=20)
ax2.set_ylabel('Population (in millions)', fontsize=14, fontweight='bold')

ax2.get_yaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'{int(x/1e6)}M')
)

ax2.grid(True, linestyle='--', alpha=0.5)
ax2.set_facecolor('#f5f5f5')

ax2.tick_params(axis='y', labelsize=12)
for label in ax2.get_yticklabels():
    label.set_fontweight('bold')

fig.set_facecolor('#ffffff')
plt.tight_layout()
plt.show()



#statistics table
summary_stats = {
    'Statistic': ['Total Countries', 'Mean Population', 'Median Population',
                  'Std Dev Population', 'Min Population', 'Max Population',
                  'Q1 (25th Percentile)', 'Q3 (75th Percentile)'],
    'Value': [
        len(population_2023),
        f"{population_2023.mean():,.0f}",
        f"{population_2023.median():,.0f}",
        f"{population_2023.std():,.0f}",
        f"{population_2023.min():,.0f}",
        f"{population_2023.max():,.0f}",
        f"{population_2023.quantile(0.25):,.0f}",
        f"{population_2023.quantile(0.75):,.0f}"
    ]
}

print("\nDetailed Summary of Population Distribution in 2023:")
print(tabulate(summary_stats, headers='keys', tablefmt='pretty', showindex=False))

#top 5 and bottom 5 countries by population
top_5 = df_2023.nlargest(5, '2023')
bottom_5 = df_2023.nsmallest(5, '2023')

# Format tables
top_5_table = top_5.copy()
top_5_table['2023'] = top_5_table['2023'].apply(lambda x: f"{x:,.0f}")
bottom_5_table = bottom_5.copy()
bottom_5_table['2023'] = bottom_5_table['2023'].apply(lambda x: f"{x:,.0f}")

print("\nTop 5 Countries by Population in 2023:")
print(tabulate(top_5_table, headers=['Country Name', 'Population (2023)'], tablefmt='pretty', showindex=False))

print("\nBottom 5 Countries by Population in 2023:")
print(tabulate(bottom_5_table, headers=['Country Name', 'Population (2023)'], tablefmt='pretty', showindex=False))