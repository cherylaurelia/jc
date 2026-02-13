#3 a)

linkedlist = [[-1, i+1 if i != 19 else -1] for i in range(20)]

firstempty = 0
firstnode = -1

#3 b)

def add(item):
    global linkedlist, firstnode, firstempty
    newnode = 0
    if firstempty == -1:
        print("cannot add, linked list is full")
        return False
    else:
        newnode = firstempty
        firstempty = linkedlist[firstempty][1]
        linkedlist[newnode][0] = item
        linkedlist[newnode][1] = firstnode
        firstnode = newnode
        return True
    
def insertdata(item1,item2,item3,item4,item5):
    global add
    add(item1)
    add(item2)
    add(item3)
    add(item4)
    add(item5)

#3 c) i)
    
def outputlinkedlist():
    global linkedlist,firstnode, firstempty
    currentpointer = 0
    currentpointer = firstnode
    while currentpointer != -1:
        print(linkedlist[currentpointer][0])
        currentpointer = linkedlist[currentpointer][1]

#3 c) ii)
insertdata(10,7,8,5,6)
outputlinkedlist()

#3 d) i)

def removedata(item):
    global linkedlist, firstempty, firstnode
    itempointer = firstnode
    olditempointer = -1

    if firstnode == -1:
        print("cannot remove, linked list empty")
        return False
    
    while itempointer != -1 and linkedlist[itempointer][0] != item:
        olditempointer = itempointer
        itempointer = linkedlist[itempointer][1]

    if itempointer == -1:
        print("item cannot be found")
        return False
    
    if olditempointer == -1:
        firstnode = linkedlist[itempointer][1]
    else:
        linkedlist[olditempointer][1] = linkedlist[itempointer][1]

    linkedlist[itempointer][1] = firstempty
    firstempty = itempointer
    linkedlist[itempointer][0] = None

#3 d) ii)
    
removedata(5)
print("after")
outputlinkedlist()
