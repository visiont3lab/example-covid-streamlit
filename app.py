import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")

fig1 = px.area(df,x="data", y=["dimessi_guariti","deceduti"], title="Andamento Nazionale")
fig2 = px.area(df,x="data", y=["nuovi_positivi"], title="Nuovi Positivi")
fig3 = px.area(df,x="data", y=["variazione_totale_positivi"], title="Variazione Positivi")
fig4 = px.line(df,x="data", y=["totale_positivi","dimessi_guariti","deceduti","totale_casi"], title="Covid19 Status")

st.title("Covid19 Dashboard")
st.dataframe(df)
st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
st.plotly_chart(fig4)

