from datetime import datetime
from classes.auto import Auto


class AutoKolcsonzo():
    def __init__(self, kolcsonzo_neve: str, auto: Auto, kolcsonzes_ideje: datetime, telefonszam: str, email_cim: str, azonosito: int):
        self.azonosito = azonosito
        self.kolcsonzo_neve = kolcsonzo_neve
        self.autok = [auto]
        self.kolcsonzes_ideje = kolcsonzes_ideje
        self.telefonszam = telefonszam
        self.email_cim = email_cim

    def kiiras(self):
        autok = ""
        
        for auto in self.autok:
            autok += f" ${auto.azonosito} - ${auto.rendszam} - ${auto.model} - ${auto.tipus}"
        
        print(f"${self.azonosito}${self.kolcsonzo_neve}${self.kolcsonzes_ideje}${self.telefonszam}${self.email_cim} - \nAutok: ${autok}")