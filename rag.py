class RAG:

    def lookup(self, q):
        q = q.lower()
        if "oro" in q:
            return "Fuente: Precio del oro y mercado forward."
        if any(x in q for x in ["nacional", "first", "dondé", "prestaprenda"]):
            return "Fuente: Análisis competitivo del sector prendario."
        if "campaña" in q:
            return "Fuente: Benchmarks de marketing prendario."
        return "Fuente: Datos históricos del sector (Profeco)."
