class BaseAgent:
    """
    Clase base simplificada para agentes en el simulador multiagente de MLS.

    En la maqueta no la usamos directamente en el motor, pero prepara
    la arquitectura para una versión más avanzada donde cada agente
    (clientes, competencia, oro, sucursales, macro, etc.) ejecuta
    decisiones autónomas basadas en reglas, ML o LLMs.
    """

    def __init__(self, name: str, agent_type: str):
        self.name = name
        self.agent_type = agent_type

    def act(self, state: dict) -> dict:
        """
        Comportamiento del agente.

        Debe recibir un estado del sistema y devolver un diccionario
        con efectos (por ejemplo, cambios en originación, ticket,
        tasas, campañas, etc.).

        En subclases reales este método se sobrescribe.
        """
        raise NotImplementedError("El agente debe implementar act() en su subclase.")
