import streamlit as st
from dashboard.loader import DataLoader
from dashboard.tabs import TabFactory

class Dashboard:
    def __init__(self):

        # Initial settings
        st.set_page_config(page_title="Dashboard: Students Social Media Addiction", layout="wide")
        st.title("📱 Social Media Impact in Students Lives")

        self.df = DataLoader.load_data()
        self.tabs = TabFactory(self.df)

    # Tabs creation
    def run(self):
        self.tabs.tab_sleep_vs_mental_health()
        self.tabs.tab_platforms_by_country()
        self.tabs.tab_usage_by_academic_level()
        self.tabs.tab_top_countries()
