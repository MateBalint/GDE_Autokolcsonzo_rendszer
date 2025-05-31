from adatgenerator import AdatGenerator
from classes.berles import Berles
from classes.menu import Menu


class AutoKolcsonzoApp:
        
    def run(self):
        adatgenerator = AdatGenerator()
        berles = Berles(adatgenerator)
        menu = Menu(berles)
        menu.run()
        
if __name__ == "__main__":
    app = AutoKolcsonzoApp()
    app.run()