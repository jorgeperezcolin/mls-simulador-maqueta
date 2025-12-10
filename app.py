import streamlit as st
import pandas as pd
from orchestrator import Orchestrator

st.set_page_config(
    page_title="Simulador MLS – Maqueta MAS",
    layout="wide",
)

orc = Orchestrator()

# ---- Sidebar ----
st.sidebar.title("Simulador Multiagente (Maqueta)")
st.sidebar.markdown("Versión demo para Comité Ejecutivo de MLS")
st.sidebar.divider()

st.sidebar.markdown("### Escenarios sugeridos")
st.sidebar.markdown("- Oro cae 3% + reapertura de Nacional")
st.sidebar.markdown("- Competencia lanza contracampaña")
st.sidebar.markdown("- MLS baja tasas en CDMX")
st.sidebar.markdown("- Campaña en zonas rojas")

st.sidebar.divider()
st.sidebar.markdown("**Business Data Scientists®**")


# ---- Main layout ----
st.title("🔮 Simulador Multiagente de MLS — Maqueta Ejecutiva")
st.markdown(
    """
    Este prototipo responde preguntas estratégicas de negocio en lenguaje natural.
    """
)

pregunta = st.text_input(
    "Escribe tu pregunta tipo '¿Qué pasa si…?'",
    placeholder="¿Qué pasa si el oro cae 3% y Nacional regresa de la huelga?",
)

boton = st.button("Simular escenario", use_container_width=True)

if boton and pregunta.strip():
    resultado = orc.process_question(pregunta)

    col1, col2 = st.columns([1.2, 1])

    # -----------------------
    # PANEL DE RESULTADOS
    # -----------------------
    with col1:
        st.subheader("📊 Resultados del escenario")
        df = pd.DataFrame(
            {
                "Variable": [
                    "Ticket promedio",
                    "Originación",
                    "Refrendos",
                    "Inventiencia",
                    "Reacción competencia",
                ],
                "Valor": [
                    resultado["resultados"]["ticket_promedio"],
                    resultado["resultados"]["originacion"],
                    resultado["resultados"]["refrendos"],
                    resultado["resultados"]["inventario"],
                    resultado["resultados"]["competencia_reaccion"],
                ],
            }
        )
        st.dataframe(df, use_container_width=True)

        # Gráfica
        st.subheader("📈 Impacto cuantitativo (visualización rápida)")
        graf = pd.DataFrame(
            {
                "Métrica": ["Ticket", "Originación", "Refrendos", "Inventario"],
                "Valor": [
                    resultado["resultados"]["ticket_promedio"],
                    resultado["resultados"]["originacion"],
                    resultado["resultados"]["refrendos"],
                    resultado["resultados"]["inventario"],
                ],
            }
        )
        st.bar_chart(graf, x="Métrica", y="Valor")

    # -----------------------
    # PANEL ESTRATEGISTA MLS
    # -----------------------
    with col2:
        st.subheader("🎯 Recomendaciones estratégicas MLS")

        for r in resultado["recomendaciones"]:
            st.markdown(f"- {r}")

        st.subheader("🧠 Explicabilidad (XAI)")
        st.markdown(resultado["xai"])

        st.subheader("📚 Fuente (RAG)")
        st.caption(resultado["resultados"]["cita_rag"])
