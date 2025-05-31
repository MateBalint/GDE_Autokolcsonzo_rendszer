from abc import ABC

class Auto(ABC):
    """
    Absztrakt Auto osztály, mely tartalmazza a különböző children osztályok által megosztott property-ket.
    """
    def __init__(self, azonosito: int, tipus: str, rendszam: str, model: str,  berleti_dij: int):
        self.azonosito = azonosito
        self.tipus = tipus
        self.rendszam = rendszam
        self.model = model
        self.berleti_dij = berleti_dij

    def info(self):
        """
        Visszaadja az Auto objektum property-jeit stringgé összefűzve.
        """
        return f"Típus: {self.tipus} - Rendszám: {self.rendszam} - Model: {self.model} - Bérleti díj: {self.berleti_dij}"