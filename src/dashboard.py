import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'data', 'banco_iot.db')
engine = create_engine(f'sqlite:///{DB_PATH}')

def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

st.set_page_config(page_title="Dashboard IoT", layout="wide")
st.title('🌡️ Dashboard de Temperaturas IoT')

st.header('Média de Temperatura por Dispositivo')
df_avg = load_data('avg_temp_por_dispositivo')
df_avg['avg_temp'] = pd.to_numeric(df_avg['avg_temp'])
# Define a coluna que será o eixo X
df_avg = df_avg.set_index('device_id')
st.bar_chart(df_avg['avg_temp'], color="#FF4B4B")

st.header('Leituras por Hora do Dia')
df_hora = load_data('leituras_por_hora')
df_hora['contagem'] = pd.to_numeric(df_hora['contagem'])
df_hora = df_hora.set_index('hora')
st.line_chart(df_hora['contagem'], color="#0068C9")

st.header('Temperaturas Máximas e Mínimas por Dia')
df_max_min = load_data('temp_max_min_por_dia')
# Organiza os dados para plotagem
df_max_min = df_max_min.set_index('data')
df_grafico = df_max_min[['temp_max', 'temp_min']]
st.line_chart(df_grafico, color=["#FF2B2B", "#0068C9"])