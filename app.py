import streamlit as st
from orchestrator import Orchestrator
from simulation_engine import SimulationEngine
from strategist import Strategist
from llm_mock import LLM  # Usa tu wrapper real
from rag import KnowledgeBase  # Usa tu implementación real

st.set_page_config(page_title="Simulador MLS", layout="wide")

# Inicialización de componentes
llm = LLM()
kb = KnowledgeBase()
engine = SimulationEngine()
strategist = Strategist(llm=llm, knowledge_base=kb)
orchestrator = Orchestrator(simulation_engine=engine, strategist=strategist)

st.title("🧠 Simulador Multiagente MLS (Maqueta)")

prompt = st.text_area("Haz una pregunta:", height=150)

if st.button("Simular"):
    if prompt.strip() == "":
        st.warning("Por favor ingresa una pregunta.")
    else:
        output = orchestrator.run_query(prompt)

        st.subheader("📊 Resultados simulados para MLS")
        st.json(output["simulation"])

        st.subheader("🧭 Recomendaciones estratégicas para MLS")
        st.write(output["recommendations"])

        st.subheader("⚔️ ¿Qué harán los competidores?")
        st.json(output["competitor_reactions"])
