from simulation_engine import SimulationEngine
from strategist import Strategist
from xai import XAI
from rag import RAG


class Orchestrator:

    def __init__(self):
        self.engine = SimulationEngine()
        self.strategist = Strategist()
        self.xai = XAI()
        self.rag = RAG()

    def _detect(self, q: str) -> dict:
        ql = q.lower()
        return {
            "oro": "%" in ql or "oro" in ql,
            "marketing": any(x in ql for x in ["campaña", "campana", "publicidad", "promo"]),
            "tasas": "tasa" in ql,
            "sucursales": any(x in ql for x in ["cdmx", "zona", "sucursal", "ageb"]),
            "mls_baja_tasa": "mls" in ql and "baja" in ql,
            "mls_sube_tasa": "mls" in ql and "sube" in ql,
            "huelga": "huelga" in ql,
            "nacional_reabre": "nacional" in ql and "reabre" in ql,
        }

    def process_question(self, question: str) -> dict:
        flags = self._detect(question)
        cita = self.rag.lookup(question)
        resultados = self.engine.run(flags, question, cita)
        recomendaciones = self.strategist.recommend(resultados, flags)
        explicacion = self.xai.explain(flags, resultados, cita)

        return {
            "resultados": resultados,
            "recomendaciones": recomendaciones,
            "xai": explicacion
        }
