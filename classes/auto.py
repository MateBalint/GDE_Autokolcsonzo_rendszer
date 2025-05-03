from abc import ABC

class Auto(ABC):
    """
    Az autó alapvető attribútumai:
   :param rendszam: Az autó rendszáma
   :param tipus: Az autó típusa/modelje
   :param berleti_dij: Napi bérleti díj
    """

    def __init__(self, azonosito: int, tipus: str, rendszam: str, model: str,  berleti_dij: int):
        self.azonosito = azonosito
        self.tipus = tipus
        self.rendszam = rendszam
        self.model = model
        self.berleti_dij = berleti_dij
