#s21qp42.py

#1 a)

class Node:
    def __init__(self, data, nextnode):
        self.__data = data #integer
        self.__nextnode = nextnode #integer

    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__nextnode
    
startpointer = 0
emptylist = 5

#1 b)
        
linkedlist = [
    Node(1,1),
    Node(5,4),
    Node(6,7),
    Node(7, -1),
    Node(2,2),
    Node(0,6),
    Node(0,8),
    Node(56,3),
    Node(0,9),
    Node(0,-1)
]

#1 c i)

def outputNodes():
    global linkedlist
    currentpointer = 0

    while currentpointer != -1:
        print(linkedlist[currentpointer].getData())
        currentpointer = linkedlist[currentpointer].getNext()

#1 c ii)
        
outputNodes()

#1 d) i)

def addnode(item):
    global linkedlist, startpointer, emptylist
    newnode = 0
    currentpointer = 0
    if emptylist == -1:
        print("cannot add, linked list full")
        return False
    
    newnode = emptylist
    emptylist = linkedlist[emptylist].getNext()

    linkedlist[newnode]._Node__data = item
    linkedlist[newnode]._Node__nextnode = -1

    if startpointer == -1:
        startpointer = newnode
    else:
        currentpointer = startpointer
        while linkedlist[currentpointer].getNext() != -1:
            currentpointer = linkedlist[currentpointer].getNext()

        linkedlist[currentpointer]._Node__nextnode = newnode

    return True

#1 d ii)

outputNodes()
if addnode(5):
    print("Sucessfully added")
else:
    print("Unsuccessful")
outputNodes()
