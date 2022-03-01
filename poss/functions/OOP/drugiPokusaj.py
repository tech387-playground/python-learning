
from ast import While
import random
from unicodedata import name

#Inheritance (koristenje koda ponovo, subclasse pozivaju konstruktor prve klase)
class cudo(object):
    def __init__(self, name, mocUdara):
        self.name = name
        self.zdravlje = 100
        self.mocUdara = mocUdara
#Abstraction
    def radnja(self):
        pass

    def dajIme(self):
        return self.name
    def dajZdravlje(self):
        return self.zdravlje
    def dajMocUdara(self):
        return self.mocUdara
    def dajStetu(self, udarniEfekt):
        return self.zdravlje - udarniEfekt
    def dajMiPodatke(self):
        return self.dajIme(), self.dajMocUdara(), self.dajZdravlje()


#Inheritance
class cudo1(cudo):
    def __init__(self):
        super().__init__("cudak1",12)
    def dajCudo(self):
        return(str(self.zdravlje) + str(self.name) +  str(self.mocUdara))
#Abstraction
    def radnja(self):
        print("ujeda")
#Inheritance
class cudo2(cudo):
    def __init__(self):
        super().__init__("cudak2",18)
    def dajCudo(self):
        return(str(self.zdravlje) + str(self.name) +  str(self.mocUdara))
#Abstraction
    def radnja(self):
        print("sisa krv")
#Inheritance
class cudo3(cudo):
    def __init__(self):
        super().__init__("cudak3",4)
#Encapsulation (kada metodom objekta mjenjamo neku klasu, sprecava slucajne izmjene podatka)
        self.zdravlje = 160
    def dajCudo(self):
        return(str(self.zdravlje) + str(self.name) +  str(self.mocUdara))
#Abstraction
    def radnja(self):
        self.oci = True
        print("bleji ocima dok ne ustrasi")
z = cudo1().dajMiPodatke()
print(z)



c1 = cudo1()
c2 = cudo2()
c3 = cudo3()
#Polymorphism (isti naziv ali razlicito stanje, radnja)
for cudoviste in (c1, c2, c3):
    print(cudoviste.dajCudo())

izabir1 = input("odaberi prvo, drugo ili trece: ")
if izabir1 == "prvo" or "drugo" or "trece":
    if izabir1 == "prvo":
        print("prvo cudoviste ce se borit protiv druga dva")
        c2.zdravlje = c2.zdravlje - c1.mocUdara
        c3.zdravlje = c3.zdravlje - c1.mocUdara
        print(c2.zdravlje, c3.zdravlje)
    if izabir1 == "drugo":
        print("drugo cudoviste ce se borit protiv druga dva")
        c1.zdravlje = c1.zdravlje - c2.mocUdara
        c3.zdravlje = c3.zdravlje - c2.mocUdara
        print(c1.zdravlje, c3.zdravlje)
    if izabir1 == "trece":
        print("trece cudoviste ce se borit protiv druga dva")
        c1.zdravlje = c1.zdravlje - c2.mocUdara
        c2.zdravlje = c2.zdravlje - c2.mocUdara
        print(c2.zdravlje, c1.zdravlje)
else:
    print("pogresan unos")

jedanVsJedan = input("odaberi: prvo ili drugo")
if jedanVsJedan == "prvo" or "drugo":
    if jedanVsJedan == "prvo":
        while c2.zdravlje > 0 and c1.zdravlje > 0:
            c1.zdravlje = c1.zdravlje - c2.mocUdara
            c2.zdravlje = c2.zdravlje - c1.mocUdara
            print(c1.zdravlje, c2.zdravlje)
        if c1.zdravlje <= 0:
            print("prvo mrtvo")
        if c2.zdravlje <= 0:
            print("drugo mrtvo")
    if jedanVsJedan == "drugo":
        while True:
            if c1.zdravlje >= 0 and c2.zdravlje >= 0:
                c2.zdravlje = c2.zdravlje - c1.mocUdara
                c1.zdravlje = c1.zdravlje - c2.mocUdara
            print("cudoviste1   " + str(c1.zdravlje), "cudoviste2   " + str(c2.zdravlje))
            if c1.zdravlje in range(20,30):
                superMoc = input("dodaj super moc, unesi Da ili Ne: ")
                if superMoc == "Da":
                    print("prije super moci stanje " + "prvo cudoviste " + str(c1.zdravlje) +"  "+ "drugo cudoviste " + str(c2.zdravlje))
                    c2.zdravlje = c2.zdravlje - (c1.mocUdara + 40)
                    print("poslije SUpera stanje" + "prvo cudoviste " + str(c1.zdravlje) +"  "+ "drugo cudoviste " + str(c2.zdravlje))
                    if c2.zdravlje <= 0:
                        print("cudoviste 2 mrtvo")
                        break
                else:
                    print("ne zeli super moci")
                    continue   
            if c2.zdravlje <= 0:
                print("drugo mrtvo")
                break
            if c1.zdravlje <= 0:
                print("prvo mrtvo")
                break
else:
    print("pogresan unos")


class OdabirNajmocnijeg():
    def dajMiCudovisteSaNajviseEnergije(self):
        if c1.dajZdravlje() > c2.dajZdravlje() and c3.dajZdravlje():
            return "prvo je najzdravije " + str(c1.dajZdravlje())
        if c2.dajZdravlje() > c1.dajZdravlje() and c3.dajZdravlje():
            return "drugo je najzdravije " + str(c2.dajZdravlje())
        if c3.dajZdravlje() > c1.dajZdravlje() and c2.dajZdravlje():
            return "trece je najzdravije " + str(c3.dajZdravlje())
najopasnije = OdabirNajmocnijeg()
print(najopasnije.dajMiCudovisteSaNajviseEnergije())