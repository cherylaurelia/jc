#a
class Balloon:
    def __init__(self, pColor, pDefenceItem):
        self.__health = 100 #int
        self.__color = pColor #str
        self.__defenceitem = pDefenceItem #str

    #b
    def GetDefenceItem(self):
        return self.__defenceitem
    
    #c
    def ChangeHealth(self, newhealth):
        self.__health += newhealth

    #d
    def CheckHealth(self):
        if self.__health > 0:
            return False
        else:
            return True
    
#e
        
inputitem = str(input("Enter a defence item: "))
inputcolor = str(input("Enter a color: "))

Balloon1 = Balloon(inputcolor,inputitem)

#f

def Defend(BalloonObject):
    inputstrength = int(input("Enter the strength of the opponent: "))
    BalloonObject.ChangeHealth(-(inputstrength))
    print(BalloonObject.GetDefenceItem())
    if BalloonObject.CheckHealth():
        print("No health remaining!")
    else: 
        print("Has health remaining!")
    
    return(BalloonObject)

#g i)
Defend(Balloon1)
