class XAI:

    def explain(self, flags, resultados, cita):
        parts = []

        if flags["oro"]:
            parts.append("Impacto modelado por variación del precio del oro.")
        if flags["marketing"]:
            parts.append("Marketing incrementa originación y refrendos.")
        if flags["tasas"]:
            parts.append("Cambio de tasas afecta percepción de valor.")

        parts.append("Se generaron reacciones tácticas por competidor.")
        parts.append(cita)

        return " ".join(parts)
