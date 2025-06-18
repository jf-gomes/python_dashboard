import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

class TabFactory:
    def __init__(self, df):
        self.df = df
        self.tab1, self.tab2, self.tab3, self.tab4 = st.tabs([
            "😴 Sleep x Mental Health",
            "🌍 Platforms By Country",
            "🎓 Daily Usage By Academic Level",
            "📊 Countries With Bigger Daily Usage"
        ])

    def tab_sleep_vs_mental_health(self):
        with self.tab1:
            st.subheader("Sleep Time (hours) x Mental Health")
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.scatterplot(data=self.df, x="Sleep_Hours_Per_Night", y="Mental_Health_Score",
                            hue="Gender", palette="Set2", alpha=0.8, ax=ax)
            sns.regplot(data=self.df, x="Sleep_Hours_Per_Night", y="Mental_Health_Score",
                        scatter=False, color="gray", ax=ax)
            ax.set_title("Sleep x Mental Health")
            st.pyplot(fig)

    def tab_platforms_by_country(self):
        with self.tab2:
            st.subheader("Top Platforms By Country")
            countries = self.df["Country"].dropna().unique()
            countries.sort()
            selected_country = st.selectbox("Selecione um país para visualizar:", countries)
            filtered_df = self.df[self.df["Country"] == selected_country]
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.countplot(data=filtered_df, y="Country", hue="Most_Used_Platform", palette="tab10", ax=ax)
            ax.set_title(f"Plataformas mais usadas em {selected_country}")
            st.pyplot(fig)


    def tab_usage_by_academic_level(self):
        with self.tab3:
            st.subheader("Average Daily Usage By Academic Level")
            data = self.df.groupby("Academic_Level")["Avg_Daily_Usage_Hours"].mean().sort_values()
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(x=data.values, y=data.index, palette="coolwarm", ax=ax)
            ax.set_title("Daily usage by academic level")
            st.pyplot(fig)

    def tab_top_countries(self):
        with self.tab4:
            st.subheader("Top Countries With Bigger Daily Usage")
            data = self.df.groupby("Country")["Avg_Daily_Usage_Hours"].mean().sort_values(ascending=False).head(10)
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(x=data.values, y=data.index, palette="mako", ax=ax)
            ax.set_title("Top 10 Countries with bigger daily usage")
            st.pyplot(fig)
