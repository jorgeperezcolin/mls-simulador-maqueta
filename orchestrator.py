import json

class Orchestrator:
    def __init__(self, simulation_engine, strategist):
        self.engine = simulation_engine
        self.strategist = strategist

    def run_query(self, user_question: str) -> dict:
        # 1. Interpretación de la pregunta → escenario estructurado
        scenario = self._interpret_query(user_question)

        # 2. Simulación
        sim_output = self.engine.run(scenario)

        # 3. Recomendaciones para MLS
        recommendations = self.strategist.recommend_actions(sim_output)

        # 4. Reacciones de los competidores
        competitor_reactions = self.strategist.predict_competitor_reactions(
            scenario
        )

        # 5. Respuesta integrada
        return {
            "simulation": sim_output["results"],
            "recommendations": recommendations,
            "competitor_reactions": competitor_reactions
        }

    def _interpret_query(self, user_question: str) -> dict:
        """
        Interpreta una pregunta en lenguaje natural y construye un escenario
        mínimo viable para la maqueta.
        """
        return {
            "pregunta": user_question,
            "variacion_oro": self._detect_gold_change(user_question),
            "accion_mls": self._detect_mls_action(user_question)
        }

    def _detect_gold_change(self, q: str):
        if "oro" in q.lower():
            return "detectado"
        return "no detectado"

    def _detect_mls_action(self, q: str):
        if "tasa" in q.lower():
            return "cambio de tasa"
        if "campaña" in q.lower():
            return "campaña de marketing"
        return "sin acción específica"
