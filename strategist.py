class Strategist:

    def recommend(self, resultados, flags):
        recs = []

        if resultados["originacion"] < 95:
            recs.append("Activar ofensiva comercial inmediata (72h).")
        else:
            recs.append("Sostener ritmo con disciplina de margen.")

        if resultados["ticket_promedio"] < 980:
            recs.append("Blindar ticket con micro-ajustes de pricing.")
        else:
            recs.append("Capturar margen incremental.")

        if flags["oro"]:
            recs.append("Monitorear oro diariamente y ajustar LTV.")

        recs.append(f"Competencia: {resultados['competencia_resumen']}")

        return recs
