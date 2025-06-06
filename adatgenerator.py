from datetime import datetime,timedelta

from models.auto import Auto
from models.autokolcsonzo import Autokolcsonzo
from models.szemelyauto import SzemelyAuto
from models.teherauto import TeherAuto

class AdatGenerator:
    """
    Osztály, amely az adatok beolvasását és a program indításánál szükséges adatok legyártását végzi.
    """
    autok: list[Auto] = []
    berlesek: list[Autokolcsonzo] = []
    berles_dictionary: dict[int, list[datetime]] = {}
    auto_azonosito_lista: list[int] = []

    def __init__(self):
        self.autok = self.import_autok()
        self.berles_generalas()

    def import_szemelyautok(self):
        """
        Az elerhétő személyautó adatok importálja fájlból. 
        """
        szemelyautok: list[Auto] = []
        with open('adatok/szemelyautok.txt', encoding='utf-8') as file:
            next(file)
            for line in file:
                tulajdonsagok = line.split(',')
                azonosito = int(tulajdonsagok[0])
                tipus = tulajdonsagok[1]
                rendszam = tulajdonsagok[2]
                model = tulajdonsagok[3]
                berleti_dij = int(tulajdonsagok[4])
                ulesek_szama = int(tulajdonsagok[5])
                legkondicionalok = tulajdonsagok[6]
                szemelyauto = SzemelyAuto(azonosito, tipus, rendszam, model, berleti_dij, ulesek_szama,
                                          legkondicionalok)
                szemelyautok.append(szemelyauto)
                self.berles_dictionary[azonosito] = []
                self.auto_azonosito_lista.append(azonosito)
                
        return szemelyautok

    def import_teherautok(self):
        """
        Az elérhető teherautó adatok importálja fájlból.
        """
        teherautok: list[Auto] = []
        with open('adatok/teherautok.txt', encoding='utf-8') as file:
            next(file)
            for line in file:
                tulajdonsagok = line.split(',')
                azonosito = int(tulajdonsagok[0])
                tipus = tulajdonsagok[1]
                rendszam = tulajdonsagok[2]
                model = tulajdonsagok[3]
                berleti_dij = int(tulajdonsagok[4])
                teherbiras = int(tulajdonsagok[5])
                teherauto = TeherAuto(azonosito, tipus, rendszam, model, berleti_dij, teherbiras)
                teherautok.append(teherauto)
                self.berles_dictionary[azonosito] = []
                self.auto_azonosito_lista.append(azonosito)

        return teherautok

    def import_autok(self):
        """
        Az összes jármű adat importálását végzi.
        """
        autok: list[Auto] = []
        try:
            autok.extend(self.import_szemelyautok())
            autok.extend(self.import_teherautok())
        except Exception as e:
            print(f"Hiba történt: ${str(e)}")
            return []

        return autok

    def berles_generalas(self):
        """
        A default bérléseket generálja le. Ezek a seed adatok.
        """
        berles1 = Autokolcsonzo(
            kolcsonzo_neve="Kovács Péter",
            auto=self.autok[0],
            kolcsonzes_ideje=self.datum_krealas(1),
            telefonszam="+36 30 123 4567",
            email_cim="kovacs.peter@gmail.hu",
            azonosito=1
        )

        self.berles_dictionary[berles1.auto.azonosito].append(berles1.kolcsonzes_ideje)

        berles2 = Autokolcsonzo(
            kolcsonzo_neve="Nagy Anna",
            auto=self.autok[1],
            kolcsonzes_ideje=self.datum_krealas(11),
            telefonszam="+36 20 765 4321",
            email_cim="nagy.anna@gmail.hu",
            azonosito=2
        )

        self.berles_dictionary[berles2.auto.azonosito].append(berles2.kolcsonzes_ideje)

        berles3 = Autokolcsonzo(
            kolcsonzo_neve="Szabó László",
            auto=self.autok[0],
            kolcsonzes_ideje=self.datum_krealas(2),
            telefonszam="+36 70 987 6543",
            email_cim="szabo.laszlo@gmail.hu",
            azonosito=3
        )

        self.berles_dictionary[berles3.auto.azonosito].append(berles3.kolcsonzes_ideje)

        berles4 = Autokolcsonzo(
            kolcsonzo_neve="Tóth Erzsébet",
            auto=self.autok[3],
            kolcsonzes_ideje=self.datum_krealas(30),
            telefonszam="+36 20 555 6666",
            email_cim="toth.erzsebet@gmail.hu",
            azonosito=4
        )

        self.berles_dictionary[berles4.auto.azonosito].append(berles4.kolcsonzes_ideje)

        self.berlesek = [berles1, berles2, berles3, berles4]

    def datum_krealas(self, plusz_napok:int):
        """
        A dátum kreálását végző metódus. Csak az év, hónap és nap adatokkal dolgozunk.
        """
        datum = datetime.now()
        ev = datum.year
        honap = datum.month
        nap = datum.day
        
        uj_datum = datetime(ev, honap, nap) + timedelta(days=plusz_napok)
        
        return uj_datum
        