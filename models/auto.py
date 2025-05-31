from abc import ABC

class Auto(ABC):
    """
    Absztrakt Auto osztaly mely tartalmazza a kulonbozo children osztalyok altal megosztott property-ket.
    """
    def __init__(self, azonosito: int, tipus: str, rendszam: str, model: str,  berleti_dij: int):
        self.azonosito = azonosito
        self.tipus = tipus
        self.rendszam = rendszam
        self.model = model
        self.berleti_dij = berleti_dij

    def info(self):
        """
        Visszaadja az Auto objektum property-jeit string-ge osszefuzve.
        :return: Objektum adatok.
        """
        return f"Tipus: {self.tipus} - Rendszam: {self.rendszam} - Model: {self.model} - Berleti dij: {self.berleti_dij}"