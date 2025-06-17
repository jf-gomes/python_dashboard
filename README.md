# 📊 Students Social Media Addiction Dashboard

Um painel interativo desenvolvido com **Python** e **Streamlit** para analisar o impacto do uso de redes sociais na vida de estudantes ao redor do mundo. O projeto permite explorar dados como tempo médio de uso, saúde mental, sono, plataformas mais utilizadas e muito mais.

---

## 🔍 Visão Geral

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

## 🚀 Tecnologias Utilizadas

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- Docker (opcional, para rodar em container)

---

## 🗂️ Estrutura do Projeto

students_social_media_addiction_dashboard/
│
├── app.py # Arquivo principal (ponto de entrada)
├── data/
│ └── students_social_media_addiction.csv
├── dashboard/
│ ├── init.py
│ ├── loader.py # Carregamento e tratamento dos dados
│ ├── tabs.py # Lógica dos gráficos e abas
│ └── main_dashboard.py # Composição e controle do dashboard
├── requirements.txt # Bibliotecas necessárias
└── README.md

---

## 📈 Funcionalidades

O dashboard contém 4 abas principais:

1. **😴 Sono x Saúde Mental**  
   Relação entre horas de sono e pontuação de saúde mental, separada por gênero.

2. **🌍 Plataformas por País**  
   Mostra quais redes sociais são mais utilizadas em cada país.

3. **🎓 Uso Diário por Nível Acadêmico**  
   Compara o tempo médio diário em redes sociais de acordo com o nível acadêmico.

4. **📊 Países com Maior Uso Diário**  
   Lista os 10 países com maiores médias de uso diário.

---

## ▶️ Como Executar

1. **Clone o repositório**

git clone https://github.com/seu-usuario/social-media-dashboard.git
cd social-media-dashboard

2. **Crie um ambiente virtual (opcional, mas recomendado)**

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3. **Instale as dependências**

pip install -r requirements.txt

4. **Execute a aplicação**

streamlit run app.py

5. **Acesse o painel no navegador**

http://localhost:8501

