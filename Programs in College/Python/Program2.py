# person is a base class

class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a


# employee is the class derived from person using single inheritance

class Employee(Person):

    def __init__(self, n, a, d, s):
        Person.__init__(self, n, a)
        self.designation = d
        self.salary = s

    def show(self):
        print("Employee Details: ")
        print(" Name: ", self.name, "\n Age:", self.age, "\n Designation:", self.designation, "\n Salary:", self.salary)


class Student:
    def __init__(self, id_, rno):
        self.studentId = id_
        self.room_no = rno


# resident is a class derived from person and student using multiple inheritance

class Resident(Person, Student):

    def __init__(self, n, a, id_, rno):
        Person.__init__(self, n, a)
        Student.__init__(self, id_, rno)

    def show(self):
        print("Resident Details:")
        print(" Name:", self.name, "\n Age: ", self.age, "\n Id:", self.studentId, "\n Room no.:", self.room_no)


# Creating objects of employee and resident classes

e1 = Employee("Sufiyan", 21, "Data Scientist", 200000)
r1 = Resident("Vivek", 20, 201900025, 203)
e1.show()
r1.show()
