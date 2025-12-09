from typing import Dict, Any
import re


class SimulationEngine:
    """Motor de simulación simplificado (una sola capa de reacción)."""

    def __init__(self):
        self.base_ticket = 1000.0
        self.base_originacion = 100.0
        self.base_refrendos = 60.0
        self.base_inventario = 80.0

    def _extraer_variacion_oro(self, pregunta: str) -> float:
        texto = pregunta.lower()
        match = re.search(r"(-?\d+(?:\.\d+)?)\s*%", texto)
        if not match:
            return 0.0

        valor = float(match.group(1))
        if any(p in texto for p in ["cae", "baja", "disminuye"]):
            valor = -abs(valor)
        elif any(p in texto for p in ["sube", "aumenta", "incrementa"]):
            valor = abs(valor)
        return valor

    def run(self, activaciones: Dict[str, bool], pregunta: str, cita: str) -> Dict[str, Any]:
        ticket = self.base_ticket
        originacion = self.base_originacion
        refrendos = self.base_refrendos
        inventario = self.base_inventario

        # Oro
        if activaciones.get("oro", False):
            delta_oro = self._extraer_variacion_oro(pregunta)
            ticket *= (1 + (delta_oro * 0.012))
            originacion *= (1 + (delta_oro * 0.015))

        # Competencia
        if activaciones.get("competencia", False):
            originacion *= 0.92
            ticket *= 0.97

        # Marketing
        if activaciones.get("marketing", False):
            originacion *= 1.08
            refrendos *= 1.03

        # Tasas
        if activaciones.get("tasas", False):
            originacion *= 1.03
            ticket *= 1.02

        # Sucursales
        if activaciones.get("sucursales", False):
            refrendos *= 1.02

        if activaciones.get("competencia", False):
            reaccion_comp = "Competidores ajustan tasa y despliegan contracampaña localizada."
        else:
            reaccion_comp = "Sin reacción competitiva significativa; MLS lidera el movimiento."

        return {
            "ticket_promedio": round(ticket, 2),
            "originacion": round(originacion, 2),
            "refrendos": round(refrendos, 2),
            "inventario": round(inventario, 2),
            "competencia_reaccion": reaccion_comp,
            "cita_rag": cita,
        }
