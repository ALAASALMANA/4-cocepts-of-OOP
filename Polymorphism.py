#Polymorphism

class Employee:
    def info(self):
        name = "ALAA"
        dept = "Software Engineer department."
        print(name + " from "+dept)
class Admin:
    def info(self):
        name = "Reemaz"
        dept = "Computer Science department."
        print(name + " from "+dept)

obj_emp = Employee()
obj_adm = Admin()
obj_emp.info()
obj_adm.info()