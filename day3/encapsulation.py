class Student:
    def __init__(self,name,age,grade):
       self.name=name
       self.grade=grade
       self.__age=age
       

    def set_age(self,age):
        self.__age=age

    def get_age(self):
        print(self.__age)




s=Student("Shivam",22,"A")
s.set_age(18)
s.get_age()


