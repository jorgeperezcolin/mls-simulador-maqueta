class RAG:
    """Simulación simple de un RAG para la maqueta."""

    def lookup(self, query: str) -> str:
        q = query.lower()
        if "oro" in q:
            return "Fuente: Evolución reciente del precio del oro y curva forward (COMEX, 2025)."
        if "nacional" in q or "first" in q or "dondé" in q or "donde" in q:
            return "Fuente: Análisis competitivo de casas de empeño en México."
        if "campaña" in q or "publicidad" in q:
            return "Fuente: Estudios sectoriales de respuesta a campañas."
        return "Fuente: Profeco y análisis histórico del sector prendario."
