#a
class Card:
    def __init__(self, pNumber, pColour):
        self.__Number = pNumber
        self.__Colour = pColour

    #b
    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

#c
cards = [] #array of type card of size 30

try:
    file = open("jc2hope/CardValues.txt", 'r')  # copy path
    line = file.readline().strip()  # strip to remove space
    while line != "":
        n = line
        c = file.readline().strip()
        cards.append(Card(n, c))
        line = file.readline().strip()
except FileNotFoundError as e:
    print(f"Not Found! {e}")

# d
selected = [False] * 30 

def ChooseCard():
    while True:
        try:
            cardinput = int(input("Select a card from 1 to 30: "))
        except:
            print("Invalid input")
            continue

        if 1 <= cardinput <= 30:
            idx = cardinput - 1
            if not selected[idx]:
                selected[idx] = True
                return idx
            else:
                print("Card already selected.")
        else:
            print("Number out of range.")


 

#e i)

Player1 = [] #array for player1 of type Card

for i in range(4):
    idx = ChooseCard() - 1
    Player1.append(cards[idx])

for card in Player1:
    print(card.GetNumber(), card.GetColour())


