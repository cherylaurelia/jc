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
    file = open("jc2hope/Characters.txt", 'r')
    line = file.readline().strip()
    while line != "" and (len(Characters) < 10):
        name = line
        xcoord = int(file.readline().strip())
        ycoord = int(file.readline().strip())
        Characters.append(Character(name, xcoord, ycoord))
        line = file.readline().strip()

except FileNotFoundError as e:
    print(f"File not found! {e}")

#e
    
nameinput = str(input("Enter a name: "))

while True:
    found = False
    for character in Characters:
        if character.GetName() == nameinput:
            found = True
            break
    if found:
        break
    nameinput = input("Enter a name: ")


for j in range(len(Characters)):
    if Characters[j].GetName() == nameinput:
        idx = j
        
#f
     
print(Characters[idx].GetX(), Characters[idx].GetY())

letterinput = str(input("Enter a direction (A, W, S, D): "))

valid = ["a", "w", "s", "d", "A", "W", "S", "D"]

while letterinput not in (valid):
    letterinput = str(input("Enter a direction (A, W, S, D): "))

lowerletterinput = letterinput.lower()

if lowerletterinput == "a":
    Characters[idx].ChangePosition(-1,0)
elif lowerletterinput == "w":
    Characters[idx].ChangePosition(0,1)
elif lowerletterinput == "s":
    Characters[idx].ChangePosition(0,-1)
elif lowerletterinput == "d":
    Characters[idx].ChangePosition(1,0)

print(Characters[idx].GetX(), Characters[idx].GetY())