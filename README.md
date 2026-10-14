# 🌡️ Pipeline de Dados IoT com Docker e Python

Projeto final da disciplina **Disruptive Architectures: IoT, Big Data e IA**. O objetivo deste projeto é construir um pipeline completo que ingere dados de sensores de temperatura IoT, armazena-os de forma estruturada e os visualiza num dashboard interativo.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Base de Dados:** PostgreSQL (via Docker) / SQLite (Fallback local)
* **Bibliotecas Python:** `pandas`, `sqlalchemy`, `streamlit`
* **Plataforma:** Docker e GitHub

## 📂 Estrutura de Pastas
```text
projeto_iot_dados/
│
├── data/          # Ficheiro CSV baixado do Kaggle e base de dados local
├── docs/          # Documentação em PDF e prints do projeto
├── src/           # Códigos fonte Python
│   ├── ingest.py      # Script de ETL e criação de Views
│   └── dashboard.py   # Aplicação Streamlit
│
├── requirements.txt
├── .gitignore
└── README.md