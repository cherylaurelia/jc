class Card:

    def __init__(self, pNumber, pColour):
        self.__Number = pNumber
        self.__Colour = pColour

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

cards = [] #array of type card of size 10

class Hand:

