from simulation_engine import SimulationEngine
from strategist import Strategist


class Orchestrator:
    """
    Coordina la simulación completa:
    - inicializa el motor
    - ejecuta el escenario
    - traduce resultados en narrativa estratégica
    """

    def __init__(self):
        self.engine = SimulationEngine()
        self.strategist = Strategist()

    def run(self, scenario: dict):
        """
        Ejecuta la simulación end-to-end
        """

        simulation_result = self.engine.simulate(scenario)
        recommendation = self.strategist.recommend(simulation_result)

        return recommendation
