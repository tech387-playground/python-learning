
from location import Location
from user import User
from department import Department
from hotel import Hotel

def create_hotel():
    print('Dobro dosli! Prvi korak je kreiranje hotela. Molimo vas da unesete osnovne informacije o hotelu.')
    name = input('Ime hotela: ')
    adress = input('Adresa hotela: ')
    return Hotel(name,adress)

def hotel_info_option():
    option = 1
    while(option!=4):
        print('1.Edit hotel name\n2.Edit hotel adress\n3.Print basic hotel informations\n4.Back to main menu')
        option = int(input('Choose option: '))
        if(option==1):
            name = input('Enter new hotel name: ')
            hotel.set_name(name)
        
        if(option==2):
            adress = input('Enter new hotel adress: ')
            hotel.set_adress(adress)

        if(option==3):
            print(hotel.get_hotel_basic_info())

        if(option==4):
            break

        if(option!=0 and option!=1 and option!=2 and option!=3 and option!=4):
            print('Pogresan unos')

def department_option():
    option = 1
    while(option!=5):
        print('1.Add new department\n2.Edit department\n3.Delete department\n4.Print all departments\n5.Back to main menu')
        option = int(input('Choose option: '))
        if(option==1):
            new_dep = input('Enter new department name: ')
            hotel.add_department(new_dep)
        
        if(option==2):
            edit_dep = input('Which department you want edit? Enter name: ')
            i=0
            index = -1
            for dep in hotel.get_departments():
                if(dep.get_department()==edit_dep):
                    index = i
                    break
                i+=1
            if(index==-1):
                print('Department is not part of this hotel!')
            else:
                new_name = input('Enter new department name: ')
                hotel.edit_department(index,new_name)
                print('Department is edited successfuly.')


        if(option==3):
            del_dep = input('Which department you want delete? Enter name: ')
            i=0
            index = -1
            for dep in hotel.get_departments():
                if(dep.get_department()==del_dep):
                    index = i
                    break
                i+=1
            if(index==-1):
                print('Department is not part of this hotel!')
            else:
                hotel.delete_department(index)
                print('Department '+del_dep+' is deleted successfuly.')


        
        if(option==4):
            print('Departments list: ')
            dep: Department
            for dep in hotel.get_departments():
                print(dep.get_department())

        if(option==5):
            break

        if(option!=0 and option!=1 and option!=2 and option!=3 and option!=4 and option!=5):
            print('Pogresan unos')

def user_option():
    option = 1
    while(option!=5):
        print('1.Add new user\n2.Edit user\n3.Delete user\n4.Print all users\n5.Back to main menu')
        option = int(input('Choose option: '))
        if(option==1):
            new_user_name = input('Enter new user name: ')
            option2 = 0
            while(option2!=1 and option2!=2 and option2!=3 and option2!=4):
                print('1.Admin\n2.Manager\n3.Team Lead\n4.Staff')
                option2=int(input('Choose user role: '))
                if(option2==1):
                    role = 'Admin'
                if(option2==2):
                    role = 'Manager'
                if(option2==3):
                    role = 'Team Lead'
                if(option2==4):
                    role = 'Staff'
                if((option2!=1 and option2!=2 and option2!=3 and option2!=4)):
                    print('Wrong input! Try again.')

            hotel.add_user(new_user_name,role)

        
        if(option==2):
            edit_user = input('Which user you want edit? Enter name: ')
            i=0
            index = -1
            for user in hotel.get_users():
                if(user.get_user_name()==edit_user):
                    index = i
                    break
                i+=1
            if(index==-1):
                print('User is not part of this hotel!')
            else:
                new_name = input('Enter new user name: ')
                option2 = 0
                while(option2!=1 and option2!=2 and option2!=3 and option2!=4):
                    print('1.Admin\n2.Manager\n3.Team Lead\n4.Staff')
                    option2=int(input('Choose user new role: '))
                    if(option2==1):
                        role = 'Admin'
                    if(option2==2):
                        role = 'Manager'
                    if(option2==3):
                        role = 'Team Lead'
                    if(option2==4):
                        role = 'Staff'
                    if((option2!=1 and option2!=2 and option2!=3 and option2!=4)):
                        print('Wrong input! Try again.')
                hotel.edit_user(index,new_name,role)
                print('User is edited successfuly.')


        if(option==3):
            del_user = input('Which user you want delete? Enter name: ')
            i=0
            index = -1
            for user in hotel.get_users():
                if(user.get_user_name()==del_user):
                    index = i
                    break
                i+=1
            if(index==-1):
                print('User is not part of this hotel!')
            else:
                hotel.delete_user(index)
                print('User '+del_user+' is deleted successfuly.')


        
        if(option==4):
            print('Users list: ')
            user: User
            for user in hotel.get_users():
                print(user.get_user_name()+' ['+user.get_user_role()+']')

        if(option==5):
            break

        if(option!=0 and option!=1 and option!=2 and option!=3 and option!=4 and option!=5):
            print('Pogresan unos')

def location_option():
    option = 1
    while(option!=5):
        print('1.Add new location\n2.Edit location\n3.Delete location\n4.Print all locations\n5.Back to main menu')
        option = int(input('Choose option: '))
        if(option==1):
            new_loc = input('Enter new Location name: ')
            hotel.add_location(new_loc)
        
        if(option==2):
            edit_loc = input('Which location you want edit? Enter name: ')
            i=0
            index = -1
            for loc in hotel.get_locations():
                if(loc.get_name()==edit_loc):
                    index = i
                    break
                i+=1
            if(index==-1):
                print('Location '+edit_loc+' is not part of this hotel!')
            else:
                option2 = 0
                while(option2!=1 and option2!=2):
                    print('1.Edit location name\n2.Add sublocation')
                    option2=int(input('Choose option: '))
                    if(option2==1):
                        new_name = input('Enter new location name: ')
                        hotel.edit_location_name(index,new_name)
                    if(option2==2):
                        new_subloc = input('Enter new sublocation: ')
                        for x in hotel.get_locations():
                            if edit_loc==x.get_name():
                                print(index)
                                hotel.edit_location_sublocations(index,new_subloc)

                    if((option2!=1 and option2!=2)):
                        print('Wrong input! Try again.')


        if(option==3):
            del_loc = input('Which location you want delete? Enter name: ')
            loc: Location
            i=0
            index = -1
            for loc in hotel.get_locations():
                if(loc.get_name()==del_loc):
                    index = i
                    break
                i+=1
            if(index==-1):
                print('Location ' + del_loc + ' is not part of this hotel!')
            else:
                hotel.delete_location(index)
                print('Location '+del_loc+' is deleted successfuly.')


        
        if(option==4):
            print('Locations list: ')
            loc: Location
            for loc in hotel.get_locations():
                loc.get_location()

        if(option==5):
            break

        if(option!=0 and option!=1 and option!=2 and option!=3 and option!=4 and option!=5):
            print('Pogresan unos')

def print_hotel():
    #HOTEL INFO
    print('{\n  "name": "'+hotel.get_name()+'"\n  "adress": "'+hotel.get_adress()+'"')

    #USER
    print('  "users":  [')
    user: User
    for user in hotel.get_users():
        print('    {\n    "name": "'+user.get_user_name()+'"')
        print('    "role": "'+user.get_user_role()+'"\n    }')
    print('  ]')

    #DEPARTMENT
    print('  "departments":  [')
    dep: Department
    for dep in hotel.get_departments():
        print('    {\n    "name": "'+dep.get_department()+'"')
        print('    }')
    print('  ]')

    #LOCATION
    print('  "locations":  [')
    loc: Location
    for loc in hotel.get_locations():
        print('    {\n    "name": "'+loc.get_name()+'"')
        print('     "sublocations":  [')
        for sub_loc in loc.get_sublocations():
            print('            "name": "'+str(sub_loc)+'"')
        print('    ]')
        print('    }')  
    print('  ]')


    print('}')

hotel = create_hotel()

option = 1
while(option!=6):
    print('1.Hotel info\n2.Departmens\n3.Users\n4.Locations\n5.Print all hotel informations\n6.Complete and close')
    option = int(input('Choose option: '))
    if(option==1):
        hotel_info_option()
    if(option==2):
        department_option()
    if(option==3):
        user_option()
    if(option==4):
        location_option()
    if(option==5):
        print_hotel()
    if(option==6):
        print('Good bye!')
    if(option!=0 and option!=1 and option!=2 and option!=3 and option!=4 and option!=5 and option!=6):
        print('Pogresan unos')