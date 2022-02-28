# WEEK 3 TASK - Object-Oriented programming
# Following task is example inspired by game developers using Object-Oriented Programming.
# Create Witcher 3 fight simulator using OOP(use all 4 oop principles i.e Inheritance, Polymorphism,
# Encapsulation and Abstraction). Program should showcase fight between Witcher and any monster
# that "appears" in the wild. Any type of monster MUST have following attributes: name,
# hit_points and lives, among others. Also each monster must be capable to take or deal damage
# among other actions. Little hint, make "Enemy" superclass and start from there.
# Choose one of the following monster types:
# Vampires(Superclass)
# Higher Vampire(Subclass)
# Bruxa(Subclass)
# Ekimmara(Subclass)
# Katakan(Subclass)
# Relicts(Superclass)
# Crones(Subclass)
# Leshen(Subclass)
# Fiend(Subclass)
# Elementa(Superclass)
# Ice Elemental(Subclass)
# Fire Elemental(Subclass)
# Earth Elemental(Subclass)
# For creativity of monster actions, attacks and similar use following link as reference: 
# https://witcher.fandom.com/wiki/The_Witcher_3_bestiary


def pick_vampir():
    i = 0
    while(i!=1 and i!=2):
        print('1. Hihger_Vampire\n2. Bruxa')
        i = int(input('Tvoj izbor je: '))
        if(i==1):
            return 1
        if(i==2):
            return 2
        if(i!=1 and i!=2):
            print('Pogresan unos!')
#Superclass
class Vampires:
    #Konstruktor
    def __init__(self,name,health,damage_given):
        self.health = health
        self.damage_given = damage_given
        self.name = name
    #Sve motode ispod su dio super klase i vaze za sve subklase.
    def get_name(self):
        return self.name

    def get_health(self):
        if(self.health>0):
            return self.health
        if(self.health<=0):
            return 0

    def get_damage_given(self):
        return self.damage_given

    def take_a_damage(self,x):
        self.health= self.health-x

    def ispisi(self):
        print('Ja sam '+self.name+'! Moj health iznosi: '+str(self.health)+'. Jacina mog udarca je: '+str(self.damage_given))   
    
    #POLIMORFIZAM
    def info(self):
        print('Ja sam '+ self.get_name())
#Subclass
class Higher_Vampire(Vampires):
    #Konstruktor
    def __init__(self,health,damage_given):
        super().__init__(self.__who_am_i(),health,damage_given)
    #Dodatna metoda koja vazi samo za ovu subklasu
    def super_power(self):
        self.damage_given*=2
    #Dodatna metoda koja vazi samo za ovu subklasu
    def __who_am_i(self):
        return 'Higher_Vampire'

    #POLIMORFIZAM
    def info(self):
        print('Ja sam '+ self.get_name())

#Subclass
class Bruxa(Vampires):
    #Konstruktor
    def __init__(self,health,damage_given):
        super().__init__(self.__who_am_i(),health,damage_given)
    #Dodatna metoda koja vazi samo za ovu subklasu
    def __who_am_i(self):
        return 'Bruxa'
    
    #POLIMORFIZAM
    def info(self):
        print('Ja sam '+ self.get_name())

#Dio programa gdje korisnik bira sa kojim vampirima ce igrati

vampir1 = Higher_Vampire(100,10)
vampir2 = Bruxa(150,15)
vampir3 = Vampires('Classic vampire',50,5)

vampir1.info()
vampir2.info()
vampir3.info()