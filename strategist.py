import json

class Strategist:
    def __init__(self, llm, knowledge_base):
        self.llm = llm
        self.kb = knowledge_base

    # ------------------------------
    #   RECOMENDACIONES PARA MLS
    # ------------------------------
    def recommend_actions(self, simulation_output):
        prompt = f"""
        Contexto: simulación del mercado prendario para MLS.

        Resultados de la simulación:
        {simulation_output}

        Devuelve 3–5 recomendaciones estratégicas para MLS,
        en lenguaje ejecutivo y orientadas a acciones concretas.
        """
        return self.llm.generate(prompt)

    # ------------------------------
    #   REACCIONES DE COMPETIDORES
    # ------------------------------
    def predict_competitor_reactions(self, scenario: dict):
        prompt = f"""
        Predice la reacción más probable de cinco competidores del mercado prendario:

        - Nacional Monte de Piedad
        - Fundación Dondé
        - First Cash
        - PrestaPrenda
        - Empeños Mexicanos

        Basado en este escenario:
        {json.dumps(scenario, ensure_ascii=False, indent=2)}

        Usa patrones reales del sector (escalas, modelos de negocio, tácticas históricas).

        Devuelve SOLO un JSON con esta estructura EXACTA:

        {{
          "Nacional Monte de Piedad": "...",
          "Fundación Dondé": "...",
          "First Cash": "...",
          "PrestaPrenda": "...",
          "Empeños Mexicanos": "..."
        }}
        """
        raw = self.llm.generate(prompt)
        return self._safe_json(raw)

    def _safe_json(self, raw: str):
        try:
            return json.loads(raw)
        except Exception:
            return {"raw_text": raw}
