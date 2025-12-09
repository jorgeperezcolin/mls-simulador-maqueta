from typing import Dict, Any, List


class Strategist:
    """Módulo 'Estratega MLS' para recomendaciones ejecutivas."""

    def recommend(self, resultados: Dict[str, Any], activaciones: Dict[str, bool]) -> List[str]:
        recs = []

        originacion = resultados["originacion"]
        ticket = resultados["ticket_promedio"]

        # Originación
        if originacion < 95:
            recs.append("Reforzar campaña digital en zonas rojas durante 72 horas.")
        elif originacion > 110:
            recs.append("Probar aumento de LTV en +1% en AGEBs rentables.")
        else:
            recs.append("Mantener intensidad de campañas y monitoreo diario.")

        # Ticket
        if ticket < 950:
            recs.append("Ajustar esquema de tasas en CDMX para evitar erosión del ticket.")
        elif ticket > 1050:
            recs.append("Evaluar subida ligera de tasa para capturar margen táctico.")
        else:
            recs.append("Mantener pricing actual, priorizar crecimiento en originación.")

        # Competencia
        if activaciones.get("competencia", False):
            recs.append("Diferenciar mensaje táctico vs. Nacional y First Cash.")

        # Zonas
        if activaciones.get("sucursales", False):
            recs.append("Priorizar sucursales con alta recurrencia.")

        # Oro
        if activaciones.get("oro", False):
            recs.append("Sincronizar ajustes de LTV con monitoreo diario del oro.")

        return recs[:5]
