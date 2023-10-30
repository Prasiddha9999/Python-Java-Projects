class Person:
    name
    age
    adreess
    email
    gender
    def __init__(self,name,age,address,email,gender):
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.gender = gender
    
class Student(Person):
    grade
    sid
    def __init__(self,name,age,address,email,gender,grade,sid):
        super().__init__(name,age,address,email,gender)
        self.grade = grade
        self.sid = sid
class Teacher(Person):
    tid
s = Student("prasiddha",20,"kohalpur","regmi@gmail.com","M","1st",111)
    
