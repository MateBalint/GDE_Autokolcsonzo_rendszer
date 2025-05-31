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
        
        auto_adatok = f"Azonosító: {self.auto.azonosito} - Rendszám: {self.auto.rendszam} - Jármű modell: {self.auto.model} - Típus: {self.auto.tipus}"
        print(f"Azonosító: {self.azonosito}\nKölcsönző neve: {self.kolcsonzo_neve}\nKölcsönzés ideje: {self.kolcsonzes_ideje.date()}\nTelefonszám: {self.telefonszam}\nEmail cím: {self.email_cim}\nAutó adatok: {auto_adatok}\n")