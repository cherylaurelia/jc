#complete: must have 2 child at each parent node
#full binary tree: full at every level
#binary search tree: numbers on left r smaller, on right bigger

class Node:
    def __init__(self, leftpointer, data, rightpointer):
        self.__leftpointer = leftpointer
        self.__data = data
        self.__rightpointer = rightpointer
    
    def GetLeft(self):
        return self.__leftpointer
    
    def GetData(self):
        return self.__data

    def GetRight(self):
        return self.__rightpointer
    
#initialise
binarytree = [
    Node(1,9,2),
    Node(3,5,4),
    Node(5,12,6),
    Node(7,3,-1),
    Node(-1,6,-1),
    Node(-1,11,-1),
    Node(-1,14,-1),
    Node(-1,2,-1)
]

rootpointer = 0

#search

def search(item):
    global binarytree, rootpointer
    currentpointer = rootpointer

    while currentpointer != -1 and binarytree[currentpointer].GetData() != item:
        if item < binarytree[currentpointer].GetLeft():
            currentpointer = binarytree[currentpointer].GetLeft()
        elif item > binarytree[currentpointer].GetRight():
            currentpointer = binarytree[currentpointer].GetRight()
    
    if currentpointer == -1:
        print("item not found")
    
    return currentpointer


search(9)
#add

def add(item):
    global binarytree, rootpointer
    
    itempointer = rootpointer

    while (binarytree[itempointer].GetLeft() != -1) or (binarytree[itempointer].GetRight() != -1):
        if item < binarytree[itempointer].GetLeft():
            itempointer = binarytree[itempointer].GetLeft()
        elif item > binarytree[itempointer].GetRight():
            itempointer = binarytree[itempointer].GetRight()
