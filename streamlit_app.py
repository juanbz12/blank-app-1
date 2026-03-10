import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard de KPIs")

data = {
    "Mes": ["Enero","Febrero","Marzo","Abril","Mayo","Junio"],
    "MRR": [10000,12000,15000,14500,18000,22000],
    "Usuarios": [2000,2400,2800,2700,3500,4200]
}

df = pd.DataFrame(data)

st.subheader("Ingresos mensuales")

fig = px.line(df, x="Mes", y="MRR", markers=True)

st.plotly_chart(fig)

st.subheader("Usuarios activos")

fig2 = px.bar(df, x="Mes", y="Usuarios")

st.plotly_chart(fig2)
