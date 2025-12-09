from typing import Dict, Any


class XAI:
    """Explicabilidad ejecutiva para la maqueta."""

    def explain(self, activaciones: Dict[str, bool], resultados: Dict[str, Any], cita_rag: str) -> str:
        piezas = []

        if activaciones.get("oro", False):
            piezas.append("El módulo de oro ajustó ticket y originación según la variación detectada.")
        if activaciones.get("competencia", False):
            piezas.append("El módulo de competencia aplicó presión en originación y ticket.")
        if activaciones.get("marketing", False):
            piezas.append("El módulo de marketing incrementó originación y refrendos.")
        if activaciones.get("tasas", False):
            piezas.append("El módulo de tasas aumentó ticket y originación por percepción de valor.")
        if activaciones.get("sucursales", False):
            piezas.append("Las menciones a zonas ajustaron refrendos por gestión local.")

        if not piezas:
            piezas.append("Escenario evaluado solo con supuestos base del sector.")

        piezas.append(f"Contexto de datos: {cita_rag}")

        return " ".join(piezas)
