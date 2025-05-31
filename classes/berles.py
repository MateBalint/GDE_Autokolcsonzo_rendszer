from datetime import datetime

from adatgenerator import AdatGenerator
from models.auto import Auto
from models.autokolcsonzo import Autokolcsonzo


class Berles():
    
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
        A berles krealasat intezi ez a metodus.
        Eloszor megnezi hogy az adott auto berelve van-e mar. Ha nincs akkor azonnal tudjuk berelni.
        Ha berelve van az auto akkor pedig a berlesek listajan iteral vegig a logika es megkeresi az adott berlest ami tartalmazza az autot. Ezutan megnezi hogy az adott idopontra berelheto-e az auto
        A program gyorsitasa erdekeben van az elozetes check a dictionary-ben, hogy megnezzuk hogy az auto berelve van-e mar.
        """
        berles_azonosito = self.legnagyobb_berles_azonosito_megszerzese() + 1
        nev = input("Kerem adja meg a nevet: ")
        auto_azonosito = int(input("Kerem adja meg az auto azonositot: "))
        ev = int(input("Kerem adja meg  a kolcsonzeshez az evet: "))
        honap = int(input("Kerem adja meg  a kolcsonzeshez az honapot: "))
        nap = int(input("Kerem adja meg  a kolcsonzeshez az napot: "))
        datum = datetime(ev, honap, nap)

        if datum in self.berles_dictionary[auto_azonosito]:
            print("Van mar meglevo berles a megadott napra igy nem lehetseges ujra kiberelni jarmuvet!")
            return
        
        telefonszam = input("Kerem adja meg a telefonszamat: ")
        email_cim = input("Kerem adja meg a email cimet: ")\
        
        berlendo_auto = None
        for auto in self.autok:
            if auto.azonosito == auto_azonosito:
                berlendo_auto = auto
                break
                
        berles = Autokolcsonzo(nev, berlendo_auto, datum, telefonszam, email_cim, berles_azonosito)
        self.berlesek.append(berles)
        self.berles_dictionary[auto_azonosito].append(datum)
    
    def berles_lemondasa(self):
        """
        A berles torleset a berles azonositoja alapjan vegzo metodus.
        """
        auto_azonosito = None
        torolni_kivant_berles = None
        
        try:
            berles_azonosito = int(input("Kerem adja meg a berles azonositojat: "))

            for berles in self.berlesek:
                if berles.azonosito == berles_azonosito:
                    torolni_kivant_berles = berles
                    auto_azonosito = berles.auto.azonosito
                    
            if torolni_kivant_berles is None:
                print("Nem letezik berles ilyen azonositoval!")
                return
            
            ev = int(input("Kerem adja meg  a berles evet: "))
            honap = int(input("Kerem adja meg  a berlesi honapot: "))
            nap = int(input("Kerem adja meg a berles napjat: "))
            datum = datetime(ev, honap, nap)

            self.berlesek.remove(torolni_kivant_berles)
            self.berles_dictionary[auto_azonosito].remove(datum)
        
        except Exception as e:
            print(f"Hiba tortent: ${str(e)}")

    def berlesek_listazasa(self):
        """
        Kiirja a berleseket a console-ra.
        """
        for berles in self.berlesek:
            berles.kiiras()
    
                
    def legnagyobb_berles_azonosito_megszerzese(self):
        """
        Az utolso berles azonositojat szerzi meg, ahhoz hogy az uj berles azonositojat meg tudjuk allapitani. Minden esetben az uj berles azonositoja a legutolso berles azonositojanak inkrementalasa eggyel.
        :return: 
        """
        utolso_berles = self.berlesek[-1]
        
        return utolso_berles.azonosito
        
    def osszes_auto_listazasa(self):
        """
        Az osszes autot tartalmazo listan vegig iteral es kiirja a console-ra az autok adatait.
        """
        for auto in self.autok:
            if hasattr(auto, "legkondicionalo"):
                print(auto.info())
            elif hasattr(auto, "teherbiras"):
                print(auto.info())