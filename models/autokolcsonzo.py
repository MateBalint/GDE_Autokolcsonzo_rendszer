from datetime import datetime
from models.auto import Auto

class Autokolcsonzo:
    """
    A Autokolcsonzo osztály, amely tartalmazza a bérléshez szükséges adatokat. Pl.: bérelt autó, bérlő neve, bérlés ideje stb.
    """
    def __init__(self, kolcsonzo_neve: str, auto: Auto, kolcsonzes_ideje: datetime, telefonszam: str, email_cim: str, azonosito: int):
        self.azonosito = azonosito
        self.kolcsonzo_neve = kolcsonzo_neve
        self.auto = auto
        self.kolcsonzes_ideje = kolcsonzes_ideje
        self.telefonszam = telefonszam
        self.email_cim = email_cim

    def kiiras(self):
        """
        Kiírja a Autokolcsonzo objektum adatait.
        """
        
        auto_adatok = f"{self.auto.azonosito} - {self.auto.rendszam} - {self.auto.model} - {self.auto.tipus}"
        
        print(f"{self.azonosito} {self.kolcsonzo_neve} {self.kolcsonzes_ideje} {self.telefonszam} {self.email_cim} - \nAuto adatok: {auto_adatok}\n")