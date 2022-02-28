

class Location:
    __name = ''
    __sublocations = []

    def __init__(self,name):
        self.__name = name

    def set_name(self,name):
        self.__name=name

    def add_sublocation(self,sublocation):
        self.__sublocations.append(sublocation)
        print('Sublokacija '+sublocation+' je dodana u department '+self.__name)

    def get_name(self):
        return self.__name
        
    def get_location(self):
        print('Location name: '+self.__name+'\n    Sublocations: ')
        for x in self.__sublocations:
            print ('               '+x)
            
"""        
var = Location('Floor 1')
var.add_sublocation('Room 101')
var.add_sublocation('Room 102')
var.add_sublocation('Room 103')
var.add_sublocation('Room 104')
var.get_location()
"""