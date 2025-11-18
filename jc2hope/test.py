class Student:
    def __init__(self, pName, pAge, pGender):
        self.sName = pName
        self.sAge = pAge
        self.sGender = pGender


student1 = Student("Alex", 22, "Male")
print(student1.sName)
