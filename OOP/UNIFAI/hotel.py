from typing import List
from location import Location
from user import User
from department import Department


class Hotel:
    __name = ''
    __adress = ''
    __locations = []
    __users = []
    __departments = []


    #Hotel info CRUD without DELETE option [nema smisla delete]   
    def __init__(self,name,adress):
        self.__name = name
        self.__adress = adress

    def get_name(self):
        return self.__name

    def get_adress(self):
        return self.__adress

    def set_name(self,name):
        self.__name = name

    def set_adress(self,adress):
        self.__adress = adress

    def get_hotel_basic_info(self):
        return 'Hotel name: '+self.__name+'. Hotel location: '+self.__adress

    #User CRUD
    def add_user(self,user_name,user_role):
        self.__users.append(User(user_name,user_role))

    def get_users(self):
        return self.__users

    def edit_user(self,index,new_user_name,new_user_role):
        self.__users[index].set_name(new_user_name)
        self.__users[index].set_role(new_user_role)

    def delete_user(self,index):
        self.__users.pop(index)

    #Department CRUD
    def add_department(self,department):
        self.__departments.append(Department(department))

    def get_departments(self):
        return self.__departments

    def edit_department(self,index,new_name):
        self.__departments[index].set_name(new_name)

    def delete_department(self,index):
        self.__departments.pop(index)
    
    #Location CRUD
    def add_location(self,location):
        self.__locations.append(Location(location))

    def get_locations(self):
        return self.__locations

    def edit_location_name(self,index,new_name):
        self.__locations[index].set_name(new_name)

    def edit_location_sublocations(self,index,new_sublocation):

        self.__locations[index].add_sublocation(new_sublocation)
        
    def delete_location(self,index):
        self.__locations.pop(index)