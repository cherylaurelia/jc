# a

class TreasureChest:

    def __init__(self, pQuestion, pAnswer, pPoints):
        self.__question = pQuestion #string
        self.__answer = pAnswer #int
        self.__points = pPoints #int

    #c i)
    def getQuestion(self):
        return self.__question
    
    #c ii)
    def checkAnswer(self, userAnswer):
        if userAnswer == self.__answer:
            return True
        elif userAnswer != self.__answer:
            return False
    #c iii)
    def getPoints(self, noofattempts):
        if noofattempts == 1:
            return self.__points
        elif noofattempts == 2:
            return (self.__points // 2)
        elif noofattempts == 3 or noofattempts == 4:
            return (self.__points // 4)
        else:
            return 0

    

#b
    
arrayTreasure = []

def readData():
    try:
        file = open("jc2hope/TreasureChestData.txt", 'r')
        line = file.readline().strip()
        while line != "":
            question = line
            answer = int(file.readline().strip())
            points = int(file.readline().strip())
            arrayTreasure.append(TreasureChest(question, answer, points))
            line = file.readline().strip()
    except FileNotFoundError as e:
        print(f"File not found! {e}")

#c iv)
        
readData()
questionnumber = int(input("Enter a question from 1 to 5: "))
answerinput = int(input("Enter your answer: "))
attemptcount = 1

while (arrayTreasure[questionnumber - 1].checkAnswer(answerinput)) == False:
    answerinput = int(input("Enter your answer: "))
    attemptcount += 1
    arrayTreasure[questionnumber - 1].checkAnswer(answerinput)

print(arrayTreasure[questionnumber - 1].getPoints(attemptcount))