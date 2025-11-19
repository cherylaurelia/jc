class Card:

    def __init__(self, pNumber, pColour):
        self.__Number = pNumber
        self.__Colour = pColour

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

cards = [] #array of type card of size 30

try:
    file = open("CardValues.txt", 'r')  # copy path
    line = file.readline().strip()  # strip to remove space
    while line != "":
        n = line
        c = file.readline().strip()
        cards.append(Card(n, c))
        line = file.readline().strip()
except FileNotFoundError as e:
    print(f"Not Found! {e}")


def ChooseCard():
    global cards
    continuefinding = True
    while continuefinding == True:
        cardinput = int(input("Select a card from 1 to 30"))
        if 1 <= cardinput <= 30:
            if cards[cardinput - 1] == True:
                print("Invalid")
            elif cards[card]


