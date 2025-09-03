# Names = []
# file = open("names.txt",'r')
# for line in file:
#     Names.append(line)

#1a

HighScoreArr = [0]*11
PlayerNameArr = [""]*11

#1b

def ReadHighScores():
    file = open("HighScores.txt",'r')
    for i in range(10):
        PlayerNameArr[i] = file.readline().strip()
        HighScoreArr[i] = file.readline().strip()
    file.close()


#1c

def OutputHighScores():
     for i in range(10):
         print(f"{PlayerNameArr[i]} {HighScoreArr[i]}")

#1d

# ReadHighScores()
# OutputHighScores()

#1ei

NewPlayerName = str(input("Enter a 3 character player name: "))
while (len(NewPlayerName))!= 3:
    NewPlayerName = str(input("Enter a 3 character player name: "))
NewHighScore = int(input("Enter the player's high score between 1 and 100000 inclusive: "))
while (NewHighScore < 1 or NewHighScore > 100000):
    NewHighScore = int(input("Enter the player's high score between 1 and 100000 inclusive: "))

#1eii

def NewList(NewPlayerName, NewHighScore):
    PlayerNameArr.append(NewPlayerName)
    HighScoreArr.append(NewHighScore)
    swap = True
    temp = 0
    strtemp = ""
    while swap:
        swap = False
        for i in range(len(HighScoreArr) - 1):
            if HighScoreArr[i] < HighScoreArr[i+1]:
                temp = HighScoreArr[i]
                HighScoreArr[i] = HighScoreArr[i+1]
                HighScoreArr[i+1] = temp
                strtemp = PlayerNameArr[i]
                PlayerNameArr[i] = PlayerNameArr[i+1]
                PlayerNameArr[i+1] = strtemp
                swap = True

#1eiii

NewList(NewPlayerName, NewHighScore)
print(HighScoreArr)
print(PlayerNameArr)
