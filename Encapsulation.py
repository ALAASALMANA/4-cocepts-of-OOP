#encapsulation

class Employee:
    def __init__(self, name):
        self.name = name  # public
        self._tel = '+966565xxxxxx'  # Protected
        self.__salsry = 1700  # Private

    def get_salary(self):
        return self.__salsry


emp1 = Employee('Alaa')

print (emp1.name)
print (emp1._tel)
print (emp1.get_salary())