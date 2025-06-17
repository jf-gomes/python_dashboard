# 📊 Python Dashboard: Analysis of Students Social Media Addiction

An interactive dashboard made with **Python** and **Streamlit** to analyze the impact of social media usage in the life of students around the world. The project allows you to explore data such as average usage time, mental health, sleep, most used platforms and more.

---

## 🔍 Overview

This project uses a data set (.csv) with information about over 700 students, with variables like:

- Average time spent in social media (daily hours)
- What was the most used platform
- Wether or not it affects the student's academic performance
- Hours of sleep per night
- Academic level
- Mental health score
- Relationship status
- Country of origin

The goal is to analyze this variables with interactive graphs.

---

## 🚀 Used Technologies

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- Docker (optional, to run the application in a container)

---

## 🗂️ Project structure

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

---

## 📈 Features

The dashboard has 4 main tabs:

1. **😴 Sleep x Mental Health**
   - Relation between hours of sleep and mental health score, separated by genre.

2. **🌍 Platforms per Country**
   - Shows what social media are most used in each country.

3. **🎓 Daily Usage per Academic Level**
   - Compares the average time spent in social media according to academic level.

4. **📊 Countries With Higher Daily Usage**
   - List top 10 countries with higher average daily usage (hours).

---

## ▶️ How to Run

1. **Clone this repo**

```
git clone https://github.com/jf-gomes/python_dashboard.git
cd python_dashboard
```

2. **Create a virtual environment (optional, but recommended)**

```
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. **Install dependecies**

```
pip install -r requirements.txt
```

4. **Run application**

```
streamlit run app.py
```

5. **Access the dashboard on your browser**

http://localhost:8501

