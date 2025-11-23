#a i)
class Card:
    def __init__(self, pNumber, pColour):
        self.__Number = pNumber #int
        self.__Colour = pColour #str

    #a ii)
    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

#a iii)
    
card1 = Card(1, "red")
card2 = Card(2, "red")
card3 = Card(3, "red")
card4 = Card(4, "red")
card5 = Card(5, "red")

card6 = Card(1, "blue")
card7 = Card(2, "blue")
card8 = Card(3, "blue")
card9 = Card(4, "blue")
card10 = Card(5, "blue")

card11 = Card(1, "yellow")
card12 = Card(2, "yellow")
card13 = Card(3, "yellow")
card14 = Card(4, "yellow")
card15 = Card(5, "yellow")


#b i)
class Hand:
    def __init__(self, pCard1, pCard2, pCard3, pCard4, pCard5):
        cards = []
        cards.append(pCard1)
        cards.append(pCard2)
        cards.append(pCard3)
        cards.append(pCard4)
        cards.append(pCard5)
        self.__cards = cards
        self.__firstcard = 0
        self.__numbercards = 5
    
    #b ii)
    def GetCard(self, inputindex):
        return self.__cards[inputindex]
    
#b iii)
    
Player1 = Hand(card1, card2, card3, card4, card11)
Player2 = Hand(card12, card13, card14, card15, card6)

#c i)

def CalculateValue(playerhand):
    score = 0
    for i in range(5):

        card = playerhand.GetCard(i)
        if card.GetColour() == "red":
            score += 5
        elif card.GetColour() == "blue":
            score += 10
        elif card.GetColour() == "yellow":
            score += 15

        score += card.GetNumber()
        
    return(score)

#c ii)
    
if (CalculateValue(Player1)) > (CalculateValue(Player2)):
    print("Player 1 wins")
elif (CalculateValue(Player1)) < (CalculateValue(Player2)):
    print("Player 2 wins")
else:
    print("Tie")


