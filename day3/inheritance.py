class Student:
    def __init__(self,name,age,grade):
       self.name=name
       self.grade=grade
       self.age=age 

    def display_info(self):
        print(self.name,self.age,self.grade)

class HighSchoolStudent(Student):
    def __init__(self,name,age,grade):
        super().__init__(name,age,grade)
    def display_info(self):
        print(f"Students name is {self.name} ,age is {self.age} and grade is {self.grade}")

# parent info display
s=Student("Shivam",22,"A")
s.display_info()

# child display info
c=HighSchoolStudent("Pranav",23,"B")
c.display_info()

