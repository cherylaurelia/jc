# class Student:
#     def __init__(self, pName, pGender, pAge):
#         self.__name = pName
#         self.__gender = pGender
#         self.__age = pAge
#
#     def getName(self):
#         return self.__name
#
#     def getGender(self):
#         return self.__gender
#
#     def getAge(self):
#         return self.__age
#
#     def setName(self, newName):
#         student1.__name = newName
#
#     def printDetails(self):
#         print(f"Student Name: {self.__name}\nStudent Age: {self.__age}\nStudent Gender: {self.__gender}")
#
#
#
# student1 = Student("Alex", "Male", 15)
# student2 = Student("Wang", "Female", 15)
#
# #student1.printDetails()
#
# studentsArr = []
# studentsArr.append(student1)
# studentsArr.append(student2)
#
# for student in studentsArr:
#     student.printDetails()
#     print()
    
# access modifiers:
# public access modifier
# private access modifier - name mangling
# protected access modifier

# print(student1._name)
# student1._name = "cait"
# print(student1._name) #wouldn't work in other langs if u use _ (protected am)

#private is __ so eg self.__name. if u do print(student1.__name) it would be an error
#data hiding is when u set attributes to private so its hidden from outside world
#all attributes private, all methods public

# print(student1.getName())
# setName(student1, "haha")
# print(student1.__name)

# parent class is called super class
# child class is called sub class / derived class
#inheritance

class Animal:
    def __init__(self, pName):
        self.__name = pName

    def makeSound(self):
        print("meowgh")


someanimal = Animal("cat")
someanimal.makeSound()

class Dog(Animal):
    def __init__(self, pName, pColor):
        Animal.__init__(self, pName)
        self.__color = pColor

    def makeSound(self):
        print("wooF") # method overriding

    def getColor(self):
        return self.__color

# animal need (self), super() dont need

dog = Dog("yura", "blonde")
dog.makeSound()

#method overloading (same method but diff number of parameters, same class)
#method overloading can refer to a lot of methods with the same name, but depending on parameters, type, different methods r executed

class Test:
    def __init__(self, pa, pb, pc):
        self.__a = pa
        self.__b = pb
        self.__c = pc

    def add(self, newa, newb):
        self.__a = newa
        self.__b = newb
        return (self.__a, self.__b)

    def add(self, newa, newb, newc):
        self.__a = newa
        self.__b = newb
        self.__c = newc


def add(a,b,c=0):
    return a + b + c

print(add(3,4,3))
