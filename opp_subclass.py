# coding = UTF-8

class SchoolMember:
    '''representing every member in school'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initializaed SchoolMenber: {})'.format(self.name))

    def tell(self):
        '''tell me all details about me'''
        print('Name: "{}" Age: "{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''a teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {:d}'.format(self.salary))

class Student(SchoolMember):
    '''a student'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized a student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {}'.format(self.marks))

t = Teacher("shrividya", 40, 30000)
s = Student("Swaroop", 25, 75)

print()

members = [t, s]

for items in members:
    items.tell()
