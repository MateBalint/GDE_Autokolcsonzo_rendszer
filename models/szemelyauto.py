from models.auto import Auto

class SzemelyAuto(Auto):
    def __init__(self, azonosito: int, tipus: str, rendszam: str, model: str, berleti_dij: int, ulesek_szama: int,
                 legkondicionalo: str):
        super().__init__(azonosito, tipus, rendszam, model, berleti_dij)
        self.ulesek_szama = ulesek_szama
        self.legkondicionalo = legkondicionalo

    def info(self):
        """
        Visszaadja a Szemelyauto objektum property-jeit string-ge osszefuzve.
        :return: Objektum adatok.
        """
        return f"Szemelyauto.\nAzonosito: {self.azonosito}\nRendszam: {self.rendszam}\nTipus: {self.tipus}\nBerleti dij: {self.berleti_dij}\nUlesek szama: {self.ulesek_szama}\nLegkondicionalo: {self.legkondicionalo}\n"
