import os
import pandas as pd
from sqlalchemy import create_engine, text

# Força o banco a ficar na pasta 'data' dentro da raiz do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

DB_PATH = os.path.join(DATA_DIR, 'banco_iot.db')
CSV_PATH = os.path.join(DATA_DIR, 'IOT-temp.csv')

print(f"Banco será criado em: {DB_PATH}")
print(f"Lendo CSV de: {CSV_PATH}")

engine = create_engine(f'sqlite:///{DB_PATH}')

# 1. Leitura do CSV
df = pd.read_csv(CSV_PATH)

# Tratamento da data
df['noted_date'] = pd.to_datetime(df['noted_date'], format='%d-%m-%Y %H:%M', errors='coerce')

# 2. Inserção no banco
print("Enviando dados para o banco SQLite...")
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
print("Dados enviados com sucesso!")

# 3. Criação das Views SQL
# 3. Criação das Views SQL
views_sql = [
    "DROP VIEW IF EXISTS avg_temp_por_dispositivo;",
    """
    CREATE VIEW avg_temp_por_dispositivo AS 
    SELECT id AS device_id, AVG(temp) as avg_temp 
    FROM temperature_readings 
    GROUP BY id 
    LIMIT 30;
    """,
    
    "DROP VIEW IF EXISTS leituras_por_hora;",
    """
    CREATE VIEW leituras_por_hora AS 
    SELECT strftime('%H', noted_date) AS hora, COUNT(*) as contagem 
    FROM temperature_readings 
    WHERE noted_date IS NOT NULL 
    GROUP BY strftime('%H', noted_date) 
    ORDER BY hora;
    """,
    
    "DROP VIEW IF EXISTS temp_max_min_por_dia;",
    """
    CREATE VIEW temp_max_min_por_dia AS 
    SELECT DATE(noted_date) AS data, MAX(temp) as temp_max, MIN(temp) as temp_min 
    FROM temperature_readings 
    WHERE noted_date IS NOT NULL 
    GROUP BY DATE(noted_date) 
    ORDER BY data;
    """
]

with engine.connect() as conn:
    for sql in views_sql:
        conn.execute(text(sql))
    conn.commit()

print("Views criadas com sucesso no arquivo do banco!")