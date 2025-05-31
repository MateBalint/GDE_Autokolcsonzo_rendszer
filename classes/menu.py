import os

class Menu:
    def __init__(self, berles):
        self.berles = berles
    
    def display_menu(self):
        print("\n===== Auto Kolcsonzo Rendszer =====")
        print("1. Auto berles")
        print("2. Berles lemondasa")
        print("3. Berlesek listazasa")
        print("4. Osszes auto listazasa")
        print("0. Kilépés")
        print("==================================")
        
    def run(self):
        print("""
        ····································································
        :    _         _    __  _    _   _ _          _   _            ___ :
        :   / \  _   _| |_ /_/ | | _(_)_(_) | ___ ___(_)_(_)_ __  ____/_/_/:
        :  / _ \| | | | __/ _ \| |/ // _ \| |/ __/ __|/ _ \| '_ \|_  / _ \ :
        : / ___ \ |_| | || (_) |   <| (_) | | (__\__ \ (_) | | | |/ / |_| |:
        :/_/__ \_\__,_|\__\___/|_|\_\\___/|_|\___|___/\___/|_| |_/___\___/ :
        :|  _ \ ___ _ __   __| |___ _______ _ __                           :
        :| |_) / _ \ '_ \ / _` / __|_  / _ \ '__|                          :
        :|  _ <  __/ | | | (_| \__ \/ /  __/ |                             :
        :|_| \_\___|_| |_|\__,_|___/___\___|_|                             :
        ····································································
        """)
        
        while True:
            self.display_menu()
            choice = input("Valassz ki egy lehetoseget: ")
            if choice == "1":
                print("\n")
                self.berles.auto_berles()
            elif choice == "2":
                print("\n")
                self.berles.berles_lemondasa()
            elif choice == "3":
                print("\n")
                self.berles.berlesek_listazasa()
            elif choice == "4":
                print("\n")
                self.berles.osszes_auto_listazasa()
            elif choice == "0":
                print("""
                __     ___         _   __  _   _ 
                \ \   / (_)___ ___| | /_/_| |_| |
                 \ \ / /| / __|_  / |/ _` | __| |
                  \ V / | \__ \/ /| | (_| | |_|_|
                   \_/  |_|___/___|_|\__,_|\__(_)
                """)
                break
            else:
                print("\nÉrvénytelen választás! Kérlek 0 és 5 között válassz.")