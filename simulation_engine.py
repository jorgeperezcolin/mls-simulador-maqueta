class SimulationEngine:
    """
    Motor de simulación simplificado para la maqueta.
    Aquí puedes integrar posteriormente modelos cuantitativos,
    elasticidades y agentes multiagente reales.
    """

    def run(self, scenario: dict) -> dict:
        results = self._simulate_internal(scenario)

        return {
            "scenario": scenario,
            "results": results
        }

    def _simulate_internal(self, scenario: dict) -> dict:
        """
        Lógica mock para la maqueta.
        Devuelve variables típicas de MLS afectadas por el escenario.
        """

        base_ticket = 1200
        base_market_share = 4.5
        base_recuperacion = 72.0

        if scenario.get("variacion_oro") == "detectado":
            ticket = base_ticket * 1.05
        else:
            ticket = base_ticket

        if scenario.get("accion_mls") == "cambio de tasa":
            market_share = base_market_share + 0.3
        elif scenario.get("accion_mls") == "campaña de marketing":
            market_share = base_market_share + 0.8
        else:
            market_share = base_market_share

        return {
            "ticket_promedio": round(ticket, 2),
            "market_share": round(market_share, 2),
            "tasa_recuperacion": base_recuperacion
        }
