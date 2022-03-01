from location import Location
from user import User
from hotel import Hotel

class Ticket:
    __title= ''
    __location: Location
    __assigne: User

    def __init__(self,title,location,user):
        self.__title = title
        self.__location = location
        self.__assigne = user

    def get_tiket(self):
        print('"ticket title": '+self.__title)
        print('"location": '+self.__location.get_name())
        print('"assigne": '+self.__assigne.get_user_name())

    def get_ticket_location(self):
        return self.__location.get_name()