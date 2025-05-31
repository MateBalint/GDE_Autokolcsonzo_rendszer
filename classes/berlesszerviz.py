from datetime import datetime
from adatgenerator import AdatGenerator
from models.autokolcsonzo import Autokolcsonzo
from models.berles import Berles

class BerlesSzerviz:
    """
    Az autóbérléshez szükséges osztály, amely egy autó bérlését egy napra tárolja.
    """
    berles: Berles

    def __init__(self, adatgenerator: AdatGenerator):
        self.berles = Berles()
        self.adatgenerator = adatgenerator
        self.berles.autok = adatgenerator.autok
        self.berles.berlesek = adatgenerator.berlesek
        self.berles.berles_dictionary = adatgenerator.berles_dictionary
        self.berles.auto_azonosito_lista = adatgenerator.auto_azonosito_lista

    def auto_berles(self):
        """
        A bérlés kreálását végzi ez a metódus.
        Először megnézi, hogy az adott autó bérelve van-e már. Ha nincs, akkor azonnal tudjuk bérelni.
        A program gyorsítása érdekében van az előzetes check a dictionary-ben, hogy megnézzük, hogy az autó bérelve van-e már.
        """
        berles_azonosito = self.legnagyobb_berles_azonosito_megszerzese() + 1
        nev = input("Kérem adja meg a nevét: ")
        auto_azonosito = int(input("Kérem adja meg az autó azonosítót: "))
        
        if auto_azonosito not in self.berles.auto_azonosito_lista:
            print("A nem létezik bérelhető autó a megadott azonosítóval!")
            return
        
        ev = int(input("Kérem adja meg  a kölcsönzéshez az évet: "))
        honap = int(input("Kérem adja meg  a kölcsönzéshez az hónapot: "))
        nap = int(input("Kérem adja meg  a kölcsönzéshez az napot: "))
        datum = datetime(ev, honap, nap)

        if datum in self.berles.berles_dictionary[auto_azonosito]:
            print("Van mar meglévő bérlés a megadott napra így nem lehetséges újra kibérelni járművet!")
            return

        mostani_datum = datetime.now()
        mostani_datum_egyszeru = datetime(mostani_datum.year, mostani_datum.month, mostani_datum.day)
        
        if datum < mostani_datum_egyszeru:
            print("A bérlés dátum nem lehet régebbi a mai napnál!")
            return
        
        telefonszam = input("Kérem adja meg a telefonszámát: ")
        email_cim = input("Kérem adja meg a email címét: ")
        berlendo_auto = None
        for auto in self.berles.autok:
            if auto.azonosito == auto_azonosito:
                berlendo_auto = auto
                break

        berles = Autokolcsonzo(nev, berlendo_auto, datum, telefonszam, email_cim, berles_azonosito)
        self.berles.berlesek.append(berles)
        self.berles.berles_dictionary[auto_azonosito].append(datum)
        print(f"\nA bérlés ára: {berlendo_auto.berleti_dij} forint.")

    def berles_lemondasa(self):
        """
        A bérlés törlését a bérlés azonosítója alapján végző metódus.
        """
        auto_azonosito = None
        torolni_kivant_berles = None
        datum = None
        try:
            berles_azonosito = int(input("Kérem adja meg a bérlés azonosítóját: "))

            for berles in self.berles.berlesek:
                if berles.azonosito == berles_azonosito:
                    torolni_kivant_berles = berles
                    auto_azonosito = berles.auto.azonosito

            if torolni_kivant_berles is None:
                print("Nem létezik bérlés ilyen azonosítóval!")
                return

            ev = int(input("Kérem adja meg  a bérlés évét: "))
            honap = int(input("Kérem adja meg a bérlési hónapot: "))
            nap = int(input("Kérem adja meg a bérlés napját: "))
            datum = datetime(ev, honap, nap)

            self.berles.berlesek.remove(torolni_kivant_berles)
            self.berles.berles_dictionary[auto_azonosito].remove(datum)

        except Exception as e:
            print(f"Hiba történt: ${str(e)}")
            print("Nem került törlésre az adott bérlés mivel hibás adatokat adott meg!")
            
            if torolni_kivant_berles not in self.berles.berlesek:
                self.berles.berlesek.append(torolni_kivant_berles)
                
            if datum not in self.berles.berles_dictionary[auto_azonosito]:
                self.berles.berles_dictionary[auto_azonosito].append(datum)

    def berlesek_listazasa(self):
        """
        Kiírja a bérléseket a console-ra.
        """
        print("Bérlések: \n")
        for berles in self.berles.berlesek:
            berles.kiiras()

    def legnagyobb_berles_azonosito_megszerzese(self):
        """
        Az utolsó bérlés azonosítóját szerzi meg, ahhoz, hogy az új bérlés azonosítóját meg tudjuk állapítani. Minden esetben az új bérlés azonosítója a legutolsó bérlés azonosítójának inkrementálása eggyel.
        """
        utolso_berles = self.berles.berlesek[-1]

        return utolso_berles.azonosito

    def osszes_auto_listazasa(self):
        """
        Az összes autót tartalmazó listán végig iterál, és kiírja a console-ra az autók adatait.
        """
        print("Gépjárművek: \n")
        for auto in self.berles.autok:
            if hasattr(auto, "legkondicionalo"):
                print(auto.info())
            elif hasattr(auto, "teherbiras"):
                print(auto.info())