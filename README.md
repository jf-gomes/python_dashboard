# 📊 Python Dashboard: Analysis of Students Social Media Addiction

:us:

An interactive dashboard made with **Python** and **Streamlit** to analyze the impact of social media usage in the life of students around the world. The project allows you to explore data such as average usage time, mental health, sleep, most used platforms and more.

:brazil:

Um painel interativo desenvolvido com **Python** e **Streamlit** para analisar o impacto do uso de redes sociais na vida de estudantes ao redor do mundo. O projeto permite explorar dados como tempo médio de uso, saúde mental, sono, plataformas mais utilizadas e muito mais.

---

## 🔍 :brazil: Visão Geral / :us: Overview

:us:

This project uses a data set (.csv) with information about over 700 students, with variables like:

- Average time spent in social media (daily hours)
- What was the most used platform
- Wether or not it affects the student's academic performance
- Hours of sleep per night
- Academic level
- Mental health score
- Relationship status
- Country of origin

The goal is to analyze this variables as interactive graphs.

:brazil:

Este projeto utiliza um conjunto de dados (.csv) contendo informações de mais de 700 estudantes, com variáveis como:

- Média de horas diárias nas redes sociais
- Qual plataforma mais utilizada
- Se afeta ou não o desempenho acadêmico
- Quantidade de horas de sono por noite
- Nível acadêmico
- Pontuação de saúde mental
- Status de relacionamento
- País de origem

O objetivo é analisar essas variáveis com gráficos dinâmicos e interativos.

---

## 🚀 :brazil: Tecnologias Utilizadas / :us: Used Technologies

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- Docker (opcional, para rodar em container)

---

## 🗂️ :brazil: Estrutura do Projeto / :us: Project structure

```
students_social_media_addiction_dashboard/
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

## 📈 :brazil: Funcionalidades / :us: Funcionalities

:us:

The dashboard has 4 main tabs:

:brazil:

O dashboard contém 4 abas principais:

1. **😴 :brazil: Sono x Saúde Mental / :us: Sleep x Mental Health**  
   Relação entre horas de sono e pontuação de saúde mental, separada por gênero.

2. **🌍 :brazil: Plataformas por País / :us: Platforms per Country**  
   Mostra quais redes sociais são mais utilizadas em cada país.

3. **🎓 :brazil: Uso Diário por Nível Acadêmico / :us: Daily Usage per Academic Level**  
   Compara o tempo médio diário em redes sociais de acordo com o nível acadêmico.

4. **📊 :brazil: Países com Maior Uso Diário / :us: Countries With Higher Daily Usage**  
   Lista os 10 países com maiores médias de uso diário.

---

## ▶️ :brazil: Como Executar / :us: How to Run

1. **:brazil: Clone o repositório / :us: Clone this repo**

```
git clone https://github.com/jf-gomes/python_dashboard.git
cd social-media-dashboard
```

2. **:brazil: Crie um ambiente virtual (opcional, mas recomendado) / :us: Create a virtual environment (optional, but recommended)**

```
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. **:brazil: Instale as dependências / :us: Install dependecies**

```
pip install -r requirements.txt
```

4. **:brazil: Execute a aplicação / :us: Run application**

```
streamlit run app.py
```

5. **:brazil: Acesse o painel no navegador / :us: Access the dashboard on your browser**

http://localhost:8501

