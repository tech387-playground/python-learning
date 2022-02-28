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

#Subclass 
class Bruxa(Vampires):
    #Konstruktor
    def __init__(self,health,damage_given):
        super().__init__(self.__who_am_i(),health,damage_given)
    #Dodatna metoda koja vazi samo za ovu subklasu
    def __who_am_i(self):
        return 'Bruxa'

#Dio programa gdje korisnik bira sa kojim vampirima ce igrati

print('Odaberi prvog vampira: ')
if(pick_vampir()==1):
    vampir1 = Higher_Vampire(100,10)
else:
    vampir1 = Bruxa(150,15)

print('Odaberi drugog vampira: ')
if(pick_vampir()==1):
    vampir2 = Higher_Vampire(100,10)
else:
    vampir2 = Bruxa(150,15)


    #PRIMJER KORISTENJA ENKAPSULACIJE

#Dio programa koji ispisuje odabrane vampire
print('Vampir 1:')
vampir1.ispisi()
print('Vampir 2:')
vampir2.ispisi()
print('\nBITKA POCINJE SAD!!!!')

#Dio programa u kojem se vodi bitka izmedju vampira
while(vampir1.get_health()>0 and vampir2.get_health()>0):
    print('\n1.Napad vampira 1\n2.Napad vampira 2\n3.Ukljuci super power')
    var = int(input('Odaberi: '))
    if(var==1):
        print(vampir1.get_name()+' napada sa: '+str(vampir1.get_damage_given()))
        print(vampir2.get_name()+' ima : '+ str(vampir2.get_health()) + 'hp prije napada.')
        vampir2.take_a_damage(int(vampir1.get_damage_given()))
        print('Poslije napada '+vampir2.get_name() + ' ima: '+str(vampir2.get_health())+'hp.')

    if(var==2):
        print(vampir2.get_name()+' napada sa: '+str(vampir2.get_damage_given()))
        print(vampir1.get_name()+' ima : '+ str(vampir1.get_health()) + 'hp prije napada.')
        vampir1.take_a_damage(int(vampir2.get_damage_given()))
        print('Poslije napada '+vampir1.get_name() + ' ima: '+str(vampir1.get_health())+'hp.')

    if(var==3):
        if(vampir1.get_name()=='Higher_Vampire'):
            vampir1.super_power()
            print(vampir1.get_name()+' ima super moc. Sada njegov napad iznosi: '+str(vampir1.get_damage_given()))
        else:
            print(vampir1.get_name()+' nema super moc.')
        
        if(vampir2.get_name()=='Higher_Vampire'):
            vampir2.super_power()
            print(vampir2.get_name()+' ima super moc. Sada njegov napad iznosi: '+str(vampir2.get_damage_given()))
        else:
            print(vampir2.get_name()+' nema super moc.')

    if(var==4):
        print('Vampir 1:')
        vampir1.ispisi()
        print('Vampir 2:')
        vampir2.ispisi()
    
    if(var!=1 and var!=2 and var!=3 and var!=4):
        print('Pogresan unos!')

#Dio koda u kojem se ispisuje pobjednik bitke
if(vampir1.get_health()==0):
    print('\nPobjednik je vampir 2. Preostali hp iznosi: '+str(vampir2.get_health()))

if(vampir2.get_health()==0):
    print('\nPobjednik je vampir 1. Preostali hp iznosi: '+str(vampir1.get_health()))