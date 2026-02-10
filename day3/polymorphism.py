class Student:
    def __init__(self,name,age):
       self.name=name
       
       self.age=age 

    def display_info(self):
        print(self.name,self.age)

class HighSchoolStudent(Student):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def display_info(self):
        print(f"Students name is {self.name} ,age is {self.age} and grade is {self.grade}")

# parent info display
s=Student("Shivam",22)


# child display info
c=HighSchoolStudent("Pranav",23,"B")


def print_student_info(obj):
    obj.display_info()

# calling print_info for parent and child
print_student_info(s)
print_student_info(c)

