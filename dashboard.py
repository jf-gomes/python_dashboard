import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Initial settings
st.set_page_config(page_title="Dashboard: Students Social Media Addiction", layout="wide")
st.title("📱 Social Media Impact in Students Lives")

# Load .csv
@st.cache_data
def load():
    return pd.read_csv("./data/students_social_media_addiction.csv")

df = load()

# Remove null values to avoid errors
df = df.dropna()

# Tabs creation
tab1, tab2, tab3, tab4 = st.tabs([
    "😴 Sleep x Mental Health",
    "🌍 Platforms By Country",
    "🎓 Daily Usage By Academic Level",
    "📊 Countries With Bigger Daily Usage"
])

# ------------------ 1st Tab ------------------
with tab1:
    st.subheader("Sleep time (hours) x Mental Health")

    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="Sleep_Hours_Per_Night",
        y="Mental_Health_Score",
        hue="Gender",
        palette="Set2",
        alpha=0.8,
        ax=ax1
    )
    sns.regplot(
        data=df,
        x="Sleep_Hours_Per_Night",
        y="Mental_Health_Score",
        scatter=False,
        color="gray",
        ax=ax1
    )
    ax1.set_title("Sleep x Mental Health")
    ax1.set_xlabel("Sleep time (hours by night)")
    ax1.set_ylabel("Mental Health Points")
    st.pyplot(fig1)

# ------------------ 2nd Tab ------------------
with tab2:
    st.subheader("Top Platforms By Country")

    # Group and count platforms by country
    platforms_by_country = df.groupby(['Country', 'Most_Used_Platform']).size().reset_index(name='count')
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.countplot(
        data=df,
        y="Country",
        hue="Most_Used_Platform",
        palette="tab10",
        order=df["Country"].value_counts().index,
        ax=ax2
    )
    ax2.set_title("Most used platforms by country")
    ax2.set_xlabel("Students quantity")
    ax2.set_ylabel("Country")
    st.pyplot(fig2)

# ------------------ 3rd Tab ------------------
with tab3:
    st.subheader("Average daily usage by academic level")

    usage_by_academic_level = df.groupby("Academic_Level")["Avg_Daily_Usage_Hours"].mean().sort_values()

    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.barplot(x=usage_by_academic_level.values, y=usage_by_academic_level.index, palette="coolwarm", ax=ax3)
    ax3.set_xlabel("Average daily usage (hours)")
    ax3.set_ylabel("Academic level")
    ax3.set_title("Daily usage by academic level")
    st.pyplot(fig3)

# ------------------ 4th Tab ------------------
with tab4:
    st.subheader("Top countries with bigger daily usage")

    average_by_country = df.groupby("Country")["Avg_Daily_Usage_Hours"].mean().sort_values(ascending=False).head(10)

    fig4, ax4 = plt.subplots(figsize=(8, 5))
    sns.barplot(x=average_by_country.values, y=average_by_country.index, palette="mako", ax=ax4)
    ax4.set_xlabel("Daily Usage Average (hours)")
    ax4.set_ylabel("Country")
    ax4.set_title("Top 10 Countries with bigger daily usage")
    st.pyplot(fig4)
