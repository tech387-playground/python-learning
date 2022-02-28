class Department:
    __name = ''

    def __init__(self,name):
        self.__name = name

    def set_name(self,name):
        self.__name=name

    def get_department(self):
        return self.__name

"""
dep = Department('Kithen')
dep.set_name('Maintenance')
dep.get_department()
"""