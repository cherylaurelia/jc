class Student:
    def __init__(self, pName, pAge, pGender):
        self.sName = pName
        self.sAge = pAge
        self.sGender = pGender


try:
    file = open("textfile.txt", 'r')              #copy path
    line = file.readline()
    print(line)
except FileNotFoundError as e:
    print(f"Not Found! {e}")
