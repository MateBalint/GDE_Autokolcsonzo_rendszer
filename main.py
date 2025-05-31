from adatgenerator import AdatGenerator
from classes.berlesszerviz import BerlesSzerviz
from classes.menu import Menu

class AutoKolcsonzoApp:
        
    def run(self):
        """
        A program fő belépési pontja.
        """
        adatgenerator = AdatGenerator()
        berles = BerlesSzerviz(adatgenerator)
        menu = Menu(berles)
        menu.run()
        
if __name__ == "__main__":
    app = AutoKolcsonzoApp()
    app.run()