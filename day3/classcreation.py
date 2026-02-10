class Student:
    def __init__(self,name,age,grade):
       self.name=name
       self.grade=grade
       self.age=age 

    def display_info(self):
        print(self.name,self.age,self.grade)



s=Student("Shivam",22,"A")
s.display_info()
