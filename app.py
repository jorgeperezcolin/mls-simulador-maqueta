import streamlit as st
import pandas as pd
from orchestrator import Orchestrator

st.set_page_config(
    page_title="Simulador MLS – Multiagente",
    layout="wide"
)

orc = Orchestrator()

st.sidebar.title("Simulador MLS")
st.sidebar.markdown("Maqueta ejecutiva – Multiagente")
st.sidebar.divider()
st.sidebar.markdown("Ejemplos:")
st.sidebar.markdown("- El oro cae 3% y Nacional reabre")
st.sidebar.markdown("- MLS baja tasas y hay contracampaña")
st.sidebar.markdown("- Campaña agresiva en CDMX")

st.title("Simulador Multiagente del Mercado Prendario")
st.markdown("El simulador estima impactos y **reacciones tácticas por competidor**.")

pregunta = st.text_input(
    "Plantea el escenario estratégico",
    placeholder="¿Qué pasa si el oro cae 3% y Nacional Monte de Piedad reabre?"
)

if st.button("Simular escenario", use_container_width=True):
    if pregunta.strip():
        resultado = orc.process_question(pregunta)

        col1, col2 = st.columns([1.4, 1])

        with col1:
            st.subheader("Impacto cuantitativo")

            df = pd.DataFrame({
                "Variable": ["Ticket promedio", "Originación", "Refrendos", "Inventario"],
                "Valor": [
                    resultado["resultados"]["ticket_promedio"],
                    resultado["resultados"]["originacion"],
                    resultado["resultados"]["refrendos"],
                    resultado["resultados"]["inventario"]
                ]
            })
            st.dataframe(df, use_container_width=True)

            st.subheader("Reacción competitiva agregada")
            st.info(resultado["resultados"]["competencia_resumen"])

            st.subheader("Qué hará cada competidor")
            rows = []
            for comp, acts in resultado["resultados"]["competidores"].items():
                rows.append({
                    "Competidor": comp,
                    "Acción 1": acts[0] if len(acts) > 0 else "",
                    "Acción 2": acts[1] if len(acts) > 1 else "",
                    "Acción 3": acts[2] if len(acts) > 2 else ""
                })
            st.dataframe(pd.DataFrame(rows), use_container_width=True)

            st.caption(resultado["resultados"]["cita_rag"])

        with col2:
            st.subheader("Recomendaciones para MLS")
            for r in resultado["recomendaciones"]:
                st.markdown(f"- {r}")

            st.subheader("Explicabilidad (XAI)")
            st.markdown(resultado["xai"])
