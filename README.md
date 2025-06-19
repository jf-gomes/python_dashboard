# 📊 Python Dashboard: Analysis of Students Social Media Addiction

## Overview

An interactive dashboard made with **Python** and **Streamlit** to analyze a .csv file containing data about the impact of social media usage in the life of students around the world.

## ▶️ How to Run

1. **Clone this repo**

```
git clone https://github.com/jf-gomes/python_dashboard.git
cd python_dashboard
```

2. **Create and activate a virtual environment (optional, but recommended)**

```
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**

```
pip install -r requirements.txt
```

4. **Run application**

```
streamlit run app.py
```

5. **Access the dashboard on your browser**

http://localhost:8501

## Used Technologies

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

## Project structure

```
python_dashboard/
│
├── app.py
├── data/
│ └── students_social_media_addiction.csv
├── dashboard/
│ ├── init.py
│ ├── loader.py
│ ├── tabs.py
│ └── main_dashboard.py
├── requirements.txt
└── README.md
```

## Author

João Gomes
[LinkedIn](https://www.linkedin.com/in/joao-v-f-gomes/)