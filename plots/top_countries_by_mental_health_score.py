import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load .csv
df = pd.read_csv("./data/students_social_media_addiction.csv")

# Check if needed columns exist
columns = ['Country', 'Mental_Health_Score']
for col in columns:
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in .csv file.")

# Drop missing values
df = df.dropna(subset=columns)

# Avarage mental health score by country
avg_by_country = df.groupby("Country")["Mental_Health_Score"].mean().sort_values(ascending=False)

# Select top 5 countries by mental health score
top_20 = avg_by_country.head(20)

# Bar graph
plt.figure(figsize=(8, 6))
sns.barplot(x=top_20.values, y=top_20.index, palette="viridis")

plt.title("Top 5 countries by mental health score")
plt.xlabel("Average Mental Health Score")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top_countries_by_mental_health_score.png")  # Saves graph as .png
plt.show()
