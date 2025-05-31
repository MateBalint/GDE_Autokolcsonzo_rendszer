from datetime import datetime

from models.auto import Auto
from models.autokolcsonzo import Autokolcsonzo

class Berles:
    def __init__(self):
        self.autok: list[Auto] = []
        self.berlesek: list[Autokolcsonzo] = []
        self.berles_dictionary: dict[int, list[datetime]] = {}
        self.auto_azonosito_lista: list[int] = []