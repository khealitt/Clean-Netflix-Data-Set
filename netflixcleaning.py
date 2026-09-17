#%%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import MultipleLocator
from tabulate import tabulate

# 1. Load dataset
df = pd.read_csv("netflix_titles.csv")

# Print initial preview
print(tabulate(df.head(), headers='keys', tablefmt='psql'))

# 2. Clean data
df.columns = df.columns.str.strip()
df.dropna(subset=['country', 'rating', 'director'], inplace=True)
df['date_added'] = pd.to_datetime(
    df['date_added'].astype(str).str.strip(), errors='coerce'
)
df['year_added'] = df['date_added'].dt.year

# 3. Aggregate top 10 directors
top_directors = df['director'].value_counts().head(10).reset_index()
top_directors.columns = ['director', 'count']

# 4. Plot
fig, ax = plt.subplots(figsize=(8, 5))

sns.barplot(
    data=top_directors,
    x='director',
    y='count',
    hue='director',
    palette='YlOrRd_r',  # Warm red-to-yellow palette
    legend=False,
    ax=ax,
)

# Titles and axis formatting
ax.set_title(
    "Top 10 most common directors showcased on netflix",
    fontsize=12,
    fontweight='bold',
    pad=12,
)
ax.set_xlabel("Director", fontsize=10)
ax.set_ylabel("Amount of movies showcased", fontsize=10)

# Set whole-number increments (0, 5, 10, 15, 20) with no decimals
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.set_ylim(0, 20)

# Prevent text cut-off
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.tight_layout()



top_countries =df['country'].value_counts().head(10).reset_index()
top_countries.columns = ['countries','count']

fig,ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    data=top_countries,
    x='countries',
    y='count',
    hue='countries',
    palette='YlOrRd_r',  # Warm red-to-yellow palette
    legend=False,
    ax=ax,
)

ax.set_title(
    "Top 10 countries with the most movies produced showcased on netflix",
    fontsize=12,
    fontweight='bold',
    pad=12,
)
ax.yaxis.set_major_locator(MultipleLocator(500))
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.tight_layout()

plt.show()


# %%
