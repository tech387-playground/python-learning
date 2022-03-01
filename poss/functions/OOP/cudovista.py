from ast import While
import random


class Vampire(object): 
 def __init__(self,nameVampira,zdravlje, vrijednostNapada):
        self.name = nameVampira
        self.zdravlje = zdravlje
        self.vrijednostNapada = vrijednostNapada

        while zdravlje:
                zdravlje = zdravlje - vrijednostNapada
                print("napao je prvi player ")
                if zdravlje <= 0:
                    zdravlje = False
                    print ("Higher killed!")
                    break
                if zdravlje > 10:
                    print ("ima jos zivota")
                    continue
                if zdravlje < 10:
                    print ("ured je gotov")
                    continue



class HigherVampire(Vampire):
            super().__init__("Higher", 200, 100)




# class Bruxa(Vampire): 
#     def __init__(self):

#         super().__init__('Bruxa')

# print(Vampire(HigherVampire, Bruxa))
# class Ekimmara(Vampires):
#     higherVampireHitPoints = 8
#     higherVampireHitPoints = True

# class Katakan(Vampires): 
#     def getName(self):
#        return "Clark Kent, Jr."