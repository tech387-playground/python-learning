class Kamion: 
    def __init__(self, tandem, kiper) -> None:
        self.tandem = tandem
        self.kiper = kiper
    def display(self) -> None:
        print(self.tandem, self.kiper)

vrsta = Kamion("MAN", "MERCEDES")
vrsta.display()