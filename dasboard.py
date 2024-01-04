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


# filtrando os dados
df_filtered = df[df["Month"] == month]


# Criando o layout

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date)


fig_prod = px.bar(df_filtered, x="Date", y="Product line",
                   color="City", title="Faturamento por tipo de produto",
                   orientation="h")
col2.plotly_chart(fig_prod)


city_total = df_filtered.groupby("City")["Total"].sum().reset_index()
fig_city = px.bar(df_filtered, x="City", y="Total", 
                  title="Faturamento por filial")
col3.plotly_chart(fig_city)


fig_kind = px.pie(df_filtered, values="Total", names="Payment", 
                  title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind)

city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, y="Rating", x="City", 
                  title="Avaliação")
col5.plotly_chart(fig_rating)

