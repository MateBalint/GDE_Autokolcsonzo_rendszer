from datetime import datetime

from classes.auto import Auto
from classes.autokolcsonzo import AutoKolcsonzo
from classes.szemelyauto import SzemelyAuto
from classes.teherauto import TeherAuto


class AdatGenerator():
    
    autok = []
    szabad_autok = []
    berlesek = []
    berelt_autok = []
    
    def __init__(self):
        self.autok = self.import_autok()
        self.berles_generalas()
        berelt_autok = self.autok[:4]
        szabad_autok = self.autok[4:]
    
    def import_autok(self):
        autok: list[Auto] = []

        try:
            with open('autok.txt', encoding='utf-8') as file:
                for line in file:
                    fields = line.split(',')
                    if fields[1] == 'SZEMELYAUTO':
                        azonosito = int(fields[0])
                        rendszam = fields[2]
                        tipus = fields[1]
                        model = fields[3]
                        berleti_dij = int(fields[4])
                        ulesek_szama = int(fields[5])
                        legkondicionalok = fields[6]

                        auto = SzemelyAuto(azonosito, tipus, rendszam, model, berleti_dij, ulesek_szama, legkondicionalok)
                        autok.append(auto)
                        
                    if fields[1] == 'TEHERAUTO':
                        rendszam = fields[2]
                        tipus = fields[1]
                        model = fields[3]
                        berleti_dij = int(fields[4])
                        teherbiras = int(fields[5])
                        azonosito = int(fields[0])
                        teherauto = TeherAuto(azonosito, tipus, rendszam, model, berleti_dij, teherbiras)
                        autok.append(teherauto)
        except Exception as e:
            print(f"Hiba tortent: ${str(e)}")
            return []

        return autok
    
    def berles_generalas(self):
        berles1 = AutoKolcsonzo(
            kolcsonzo_neve="Kovács Péter",
            auto=self.berelt_autok[0],
            kolcsonzes_ideje=datetime(2025, 5, 10, 9, 0),
            telefonszam="+36 30 123 4567",
            email_cim="kovacs.peter@gmail.hu",
            azonosito=101
        )

        berles2 = AutoKolcsonzo(
            kolcsonzo_neve="Nagy Anna",
            auto=self.berelt_autok[1],
            kolcsonzes_ideje=datetime(2025, 5, 11, 14, 30),
            telefonszam="+36 20 765 4321",
            email_cim="nagy.anna@gmail.hu",
            azonosito=102
        )

        berles3 = AutoKolcsonzo(
            kolcsonzo_neve="Szabó László",
            auto=self.berelt_autok[2],
            kolcsonzes_ideje=datetime(2025, 5, 12, 8, 15),
            telefonszam="+36 70 987 6543",
            email_cim="szabo.laszlo@gmail.hu",
            azonosito=103
        )

        berles4 = AutoKolcsonzo(
            kolcsonzo_neve="Tóth Erzsébet",
            auto=self.berelt_autok[3],
            kolcsonzes_ideje=datetime(2025, 5, 13, 16, 45),
            telefonszam="+36 20 555 6666",
            email_cim="toth.erzsebet@gmail.hu",
            azonosito=104
        )
        
        self.berlesek = [berles1, berles2, berles3, berles4]