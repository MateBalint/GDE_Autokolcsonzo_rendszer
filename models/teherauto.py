from models.auto import Auto


class TeherAuto(Auto):
    def __init__(self, azonosito: id, tipus: str, rendszam: str, model:str,  berleti_dij: int, teherbiras: int):
        super().__init__(azonosito, tipus, rendszam, model, berleti_dij)
        self.teherbiras = teherbiras

    def info(self):
        """
        Visszaadja a Teherauto objektum property-jeit string-ge osszefuzve.
        :return: Objektum adatok.
        """
        return f"Teherauto.\nAzonosito: {self.azonosito}\nRendszam: {self.rendszam}\nTipus: {self.tipus}\nBerleti dij: {self.berleti_dij}\nTeher biras: {self.teherbiras}\n"
