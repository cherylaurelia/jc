#a
class Character:
    def __init__(self, pName, pXcoord, pYcoord):
        self.__name = pName #str
        self.__xcoord = pXcoord #int
        self.__ycoord = pYcoord #int
        
    #b
    def GetName(self):
        return self.__name
        
    def GetX(self):
        return self.__xcoord
        
    def GetY(self):
        return self.__ycoord
    #c 
    def ChangePosition(self, xchange, ychange):
        self.__xcoord += xchange
        self.__ycoord += ychange
        
#d

Characters = []

try:
    file = open("Characters.txt", 'r')
    line = file.readline().strip()
    while line != "":
        name = line
        xcoord = file.readline().strip()
        ycoord = file.readline.strip()
        Characters.append(Character(name, xcoord, ycoord))
        line = file.readline().strip()

except FileNotFoundError as e:
    print(f"File not found! {e}")
        
