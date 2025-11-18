class Student:
    def __init__(self, pName, pAge, pGender):
        self.__sName = pName
        self.__sAge = pAge
        self.__sGender = pGender

    def getName(self):
        return self.__sName

    def getAge(self):
        return self.__sAge

    def getGender(self):
        return self.__sGender


students = []  # student array of type Student of size 3

try:
    file = open("textfile.txt", 'r')  # copy path
    line = file.readline().strip()  # strip to remove space
    while line != "":
        sn = line
        sa = file.readline().strip()
        sg = file.readline().strip()
        students.append(Student(sn, sa, sg))
        line = file.readline().strip()
except FileNotFoundError as e:
    print(f"Not Found! {e}")

for i in range(3):
    print(students[i].getName())
    print(students[i].getAge())
    print(students[i].getGender())
