from datetime import datetime
from adatgenerator import AdatGenerator
from models.auto import Auto
from models.autokolcsonzo import Autokolcsonzo

class Berles:
    """
    Az autóbérléshez szükséges osztály, amely egy autó bérlését egy napra tárolja.
    """
    autok: list[Auto] = []
    berlesek: list[Autokolcsonzo] = []
    berles_dictionary: dict[int, list[datetime]] = {}

    def __init__(self, adatgenerator: AdatGenerator):
        self.adatgenerator = adatgenerator
        self.autok = adatgenerator.autok
        self.berlesek = adatgenerator.berlesek
        self.berles_dictionary = adatgenerator.berles_dictionary

    def auto_berles(self):
        """
        A bérlés kreálását végzi ez a metódus.
        Először megnézi, hogy az adott autó bérelve van-e már. Ha nincs, akkor azonnal tudjuk bérelni.
        A program gyorsítása érdekében van az előzetes check a dictionary-ben, hogy megnézzük, hogy az autó bérelve van-e már.
        """
        berles_azonosito = self.legnagyobb_berles_azonosito_megszerzese() + 1
        nev = input("Kérem adja meg a nevét: ")
        auto_azonosito = int(input("Kérem adja meg az autó azonosítót: "))
        ev = int(input("Kérem adja meg  a kölcsönzéshez az évet: "))
        honap = int(input("Kérem adja meg  a kölcsönzéshez az hónapot: "))
        nap = int(input("Kérem adja meg  a kölcsönzéshez az napot: "))
        datum = datetime(ev, honap, nap)

        if datum in self.berles_dictionary[auto_azonosito]:
            print("Van mar meglévő bérlés a megadott napra így nem lehetséges újra kibérelni járművet!")
            return

        telefonszam = input("Kérem adja meg a telefonszámát: ")
        email_cim = input("Kérem adja meg a email címét: ")
        berlendo_auto = None
        for auto in self.autok:
            if auto.azonosito == auto_azonosito:
                berlendo_auto = auto
                break

        berles = Autokolcsonzo(nev, berlendo_auto, datum, telefonszam, email_cim, berles_azonosito)
        self.berlesek.append(berles)
        self.berles_dictionary[auto_azonosito].append(datum)
        print(f"A bérlés ára: ${berlendo_auto.berleti_dij}")

    def berles_lemondasa(self):
        """
        A bérlés törlését a bérlés azonosítója alapján végző metódus.
        """
        auto_azonosito = None
        torolni_kivant_berles = None

        try:
            berles_azonosito = int(input("Kérem adja meg a bérlés azonosítóját: "))

            for berles in self.berlesek:
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

            self.berlesek.remove(torolni_kivant_berles)
            self.berles_dictionary[auto_azonosito].remove(datum)

        except Exception as e:
            print(f"Hiba történt: ${str(e)}")

    def berlesek_listazasa(self):
        """
        Kiírja a bérléseket a console-ra.
        """
        for berles in self.berlesek:
            berles.kiiras()

    def legnagyobb_berles_azonosito_megszerzese(self):
        """
        Az utolsó bérlés azonosítóját szerzi meg, ahhoz, hogy az új bérlés azonosítóját meg tudjuk állapítani. Minden esetben az új bérlés azonosítója a legutolsó bérlés azonosítójának inkrementálása eggyel.
        """
        utolso_berles = self.berlesek[-1]

        return utolso_berles.azonosito

    def osszes_auto_listazasa(self):
        """
        Az összes autót tartalmazó listán végig iterál, és kiírja a console-ra az autók adatait.
        """
        for auto in self.autok:
            if hasattr(auto, "legkondicionalo"):
                print(auto.info())
            elif hasattr(auto, "teherbiras"):
                print(auto.info())
