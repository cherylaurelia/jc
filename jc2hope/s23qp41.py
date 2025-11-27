#a i)
class Vehicle:

    def __init__(self, pID, pMaxSpeed, pCurrentSpeed, pIncreaseAmount, pHorizontalPosition):
        self.__id = pID
        self.__maxspeed = pMaxSpeed
        self.__currentspeed = 0
        self.__increaseamount = pIncreaseAmount
        self.__horizontalposition = 0

    #a ii)
    def GetCurrentSpeed(self):
        return self.__currentspeed

    def GetIncreaseAmount(self):
        return self.__increaseamount

    def GetMaxSpeed(self):
        return self.__maxspeed

    def GetHorizontalPosition(self):
        return self.__horizontalposition

    #a iii)

    def SetCurrentSpeed(self, new):
        self.__currentspeed = new

    def SetHorizontalPosition(self, new):
        self.__horizontalposition = new

    #a iv)

    def IncreaseSpeed(self):
        self.__currentspeed += self.__increaseamount
        self.__horizontalposition += self.__currentspeed

        if self.__currentspeed > self.__maxspeed:
            self.__currentspeed = self.__maxspeed

#b

class Helicopter(Vehicle):




