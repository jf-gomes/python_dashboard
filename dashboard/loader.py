import pandas as pd
import streamlit as st

class DataLoader:
    @staticmethod
    @st.cache_data
    # Load .csv
    def load_data():
        df = pd.read_csv("./data/students_social_media_addiction.csv")
        return df.dropna()
