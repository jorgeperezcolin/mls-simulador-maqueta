import os
import sys

# -------------------------------------
# Fix de PYTHONPATH para Streamlit Cloud
# -------------------------------------
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

# -------------------------------------
# Imports estándar
# -------------------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from orchestrator import run_simulation


# =====================================
# Configuración general
# =====================================
st.set_page_config(
    page_title="Simulador Estratégico Prendario",
    layout="wide"
)

st.title("Simulador Estratégico del Mercado Prendario")
st.markdown(
    "Herramienta de simulación de escenarios macroeconómicos y "
    "reacciones competitivas para soporte a decisiones estratégicas."
)


# =====================================
# Función: Gráfica del oro + curva forward
# =====================================
def plot_gold_forward():
    data = {
        "Mes": [
            "Spot"
