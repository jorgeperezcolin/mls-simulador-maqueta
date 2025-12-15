import re


class SimulationEngine:

    def __init__(self):
        self.ticket = 1000
        self.originacion = 100
        self.refrendos = 60
        self.inventario = 80

        self.competidores = [
            "Nacional Monte de Piedad",
            "First Cash",
            "Fundación Dondé",
            "PrestaPrenda",
            "Empeños Mexicanos"
        ]

    def _delta_oro(self, q):
        m = re.search(r"(-?\d+(?:\.\d+)?)\s*%", q)
        return float(m.group(1)) if m else 0.0

    def _acciones_competidores(self, flags, q):
        acciones = {}
        delta_oro = self._delta_oro(q)

        for c in self.competidores:
            acts = []

            if flags["oro"]:
                acts.append(
                    "Ajusta aforo/LTV por volatilidad del oro."
                    if delta_oro < 0 else
                    "Relaja aforo para capturar originación."
                )

            if flags["mls_baja_tasa"]:
                acts.append(
                    "Responde con ajuste táctico de tasa."
                    if c in ["First Cash", "PrestaPrenda"]
                    else "Compensa con promociones de refrendo."
                )

            if flags["marketing"]:
                acts.append(
                    "Despliega contracampaña digital focalizada."
                    if c in ["First Cash", "PrestaPrenda"]
                    else "Refuerza promociones en sucursal."
                )

            if flags["nacional_reabre"] and c == "Nacional Monte de Piedad":
                acts.append("Reabre con campaña de recuperación de clientes.")

            if not acts:
                acts.append("Monitorea mercado sin acción agresiva.")

            acciones[c] = acts[:3]

        return acciones

    def run(self, flags, question, cita):

        ticket = self.ticket
        originacion = self.originacion
        refrendos = self.refrendos
        inventario = self.inventario

        if flags["oro"]:
            d = self._delta_oro(question)
            ticket *= (1 + d * 0.01)
            originacion *= (1 + d * 0.015)

        if flags["marketing"]:
            originacion *= 1.08
            refrendos *= 1.03

        if flags["tasas"]:
            originacion *= 1.03

        comp = self._acciones_competidores(flags, question)

        resumen = (
            "Reacción competitiva alta y coordinada."
            if sum(len(v) for v in comp.values()) > 7
            else "Reacción competitiva moderada."
        )

        return {
            "ticket_promedio": round(ticket, 2),
            "originacion": round(originacion, 2),
            "refrendos": round(refrendos, 2),
            "inventario": round(inventario, 2),
            "competidores": comp,
            "competencia_resumen": resumen,
            "cita_rag": cita
        }
