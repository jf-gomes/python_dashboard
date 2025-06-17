import pandas as pd
import streamlit as st

class DataLoader:

    def __init__(self):
        pass

    @st.cache_data
    # Loads .csv
    def load_data(self):
        df = pd.read_csv("./data/students_social_media_addiction.csv")
        return df.dropna()

    # Returns dataframe
    def get_data(self):
        return self.load_data()
