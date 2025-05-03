from classes.auto import Auto


class TeherAuto(Auto):
    def __init__(self, azonosito: id, tipus: str, rendszam: str, model:str,  berleti_dij: int, teherbiras: int):
        super().__init__(azonosito, tipus, rendszam, model, berleti_dij)
        self.teherbiras = teherbiras

    def info(self):
        return f"Teherauto. Rendszam: {self.rendszam}\nTipus: {self.tipus}\nBerleti dij: {self.berleti_dij}\nTeher biras: {self.teherbiras}"
