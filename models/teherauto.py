from models.auto import Auto

class TeherAuto(Auto):
    def __init__(self, azonosito: id, tipus: str, rendszam: str, model:str,  berleti_dij: int, teherbiras: int):
        super().__init__(azonosito, tipus, rendszam, model, berleti_dij)
        self.teherbiras = teherbiras

    def info(self):
        """
        Visszaadja a TeherAuto objektum property-jeit stringgé összefűzve.
        """
        return f"Azonosító: {self.azonosito}\nRendszám: {self.rendszam}\nTípus: {self.tipus}\nModell: {self.model}\nBérleti díj: {self.berleti_dij} forint\nTeherbírás: {self.teherbiras}kg\n"
