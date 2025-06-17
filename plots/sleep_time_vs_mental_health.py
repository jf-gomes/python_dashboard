import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load .csv
df = pd.read_csv("./data/students_social_media_addiction.csv")

# Check columns
columns = ['Sleep_Hours_Per_Night', 'Mental_Health_Score']
for col in columns:
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in .csv file.")

# Drop missing values
df = df.dropna(subset=columns)

# Sleeping x metal health
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df,
                x='Sleep_Hours_Per_Night',
                y='Mental_Health_Score',
                hue='Gender', # optional, shows it by gender
                palette='Set2')

# Tendecy line
sns.regplot(data=df,
            x='Sleep_Hours_Per_Night',
            y='Mental_Health_Score',
            scatter=False,
            color='gray',
            line_kws={'linewidth': 2})

plt.title("Sleep time (hours) and Mental health")
plt.xlabel("Sleep time per night (hours)")
plt.ylabel("Mental health points")
plt.grid(True)
plt.tight_layout()
plt.savefig("sleep_time_vs_mental_health.png")  # Saves graph as .png
plt.show()
