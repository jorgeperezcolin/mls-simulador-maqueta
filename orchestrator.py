from simulation_engine import SimulationEngine
from strategist import Strategist
from xai import XAI
from rag import RAG


class Orchestrator:
    """Orquestador de la maqueta.
    - Interpreta la pregunta (versión reglas simples).
    - Activa componentes de simulación, recomendación y XAI.
    """

    def __init__(self):
        self.engine = SimulationEngine()
        self.strategist = Strategist()
        self.xai = XAI()
        self.rag = RAG()

    def _classify(self, question: str) -> dict:
        q = question.lower()
        return {
            "oro": ("oro" in q) or ("%" in q),
            "competencia": any(x in q for x in ["nacional", "first cash", "dondé", "donde", "fundación", "fundacion"]),
            "marketing": any(x in q for x in ["campaña", "campana", "whatsapp", "publicidad"]),
            "tasas": "tasa" in q or "tasas" in q,
            "sucursales": any(x in q for x in ["sucursal", "sucursales", "zonas", "cdmx", "zona"])
        }

    def process_question(self, question: str) -> dict:
        activaciones = self._classify(question)
        cita = self.rag.lookup(question)

        resultados = self.engine.run(activaciones, question, cita)
        recomendaciones = self.strategist.recommend(resultados, activaciones)
        explicacion = self.xai.explain(activaciones, resultados, cita)

        return {
            "resultados": resultados,
            "recomendaciones": recomendaciones,
            "xai": explicacion,
        }
