import streamlit as st
import pandas as pd

# criando os graficos com o plotly
import plotly.express as px

st.set_page_config(layout="wide")


# Com uma visão mensal 
#faturmaneto por unidade...
# tipo de produto mais vendido, contribuição por filial
# desempemnho de forma de pagamento
#Como estão as avaliações das filiais


df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")

# Criando o sidebar

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Selecione o mês desejado", df["Month"].unique())

df_filtered = df[df["Month"] == month]
df_filtered


