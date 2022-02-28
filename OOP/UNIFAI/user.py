

class User:
    __name = ''
    __role = ''

    def __init__(self,name,role):
        self.__name = name
        self.__role = role

    def set_name(self,name):
        self.__name=name

    def set_role(self,role):
        self.__role=role

    def get_user_name(self):
        return self.__name

    def get_user_role(self):
        return self.__role
    
"""
portir = User('Semso','Admin')
portir.set_name('Vedin')
portir.set_role('Manager')
portir.get_user()
"""