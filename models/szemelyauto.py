from models.auto import Auto

class SzemelyAuto(Auto):
    def __init__(self, azonosito: int, tipus: str, rendszam: str, model: str, berleti_dij: int, ulesek_szama: int,
                 legkondicionalo: str):
        super().__init__(azonosito, tipus, rendszam, model, berleti_dij)
        self.ulesek_szama = ulesek_szama
        self.legkondicionalo = legkondicionalo

    def info(self):
        """
        Visszaadja a SzemelyAuto objektum property-jeit stringgé összefűzve.
        """
        return f"Személyautó.\nAzonosító: {self.azonosito}\nRendszám: {self.rendszam}\nTípus: {self.tipus}\nBérleti díj: {self.berleti_dij}\nÜlések száma: {self.ulesek_szama}\nLégkondícionáló: {self.legkondicionalo}\n"
