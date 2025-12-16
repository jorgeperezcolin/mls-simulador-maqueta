import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from orchestrator import run_simulation


# =====================================
# Configuración general de la aplicación
# =====================================
st.set_page_config(
    page_title="Simulador Estratégico Prendario",
    layout="wide"
)

st.title("Simulador Estratégico del Mercado Prendario")
st.markdown(
    "Herramienta de simulación de escenarios macroeconómicos y reacciones "
    "competitivas para soporte a decisiones estratégicas."
)


# =====================================
# Función: Gráfica del oro + curva forward
# =====================================
def plot_gold_forward():
    data = {
        "Mes": [
            "Spot", "1M", "2M", "3M", "4M", "5M",
            "6M", "7M", "8M", "9M", "10M", "11M", "12M"
        ],
        "Precio_USD_oz": [
            4009.8, 4050, 4080, 4100, 4120, 4140,
            4160, 4170, 4180, 4190, 4200, 4210, 4250
        ]
    }

    df = pd.DataFrame(data)

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(df["Mes"], df["Precio_USD_oz"], marker="o")

    ax.set_title("Precio del Oro Spot + Curva Forward (12 meses)")
    ax.set_xlabel("Horizonte temporal")
    ax.set_ylabel("USD / onza")

    ax.grid(True, alpha=0.3)

    return fig


# =====================================
# Definición del escenario
# =====================================
st.subheader("Definición del escenario")

gold_change = st.slider(
    "Variación porcentual del precio del oro",
    min_value=-10,
    max_value=10,
    value=0,
    step=1
)

inflation = st.selectbox(
    "Nivel de inflación",
    ["Baja", "Media", "Alta"]
)

unemployment = st.selectbox(
