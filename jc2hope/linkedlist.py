#linkedlist.py

data = [None for _ in range (10)]
pointer = [i+1 if i != 9 else -1 for i in range(10)]

startpointer = -1 
heappointer = 0
temp = 0
itempointer = 0
olditempointer = -1
temppointer = 0

#output

def out():
    global data, pointer
    print(data)
    print(pointer)
    print(f"start pointer : {startpointer}")
    print(f"heap pointer : {heappointer}")

#add 

def add(item):
    global data,pointer, startpointer, heappointer, temp
    if heappointer == -1:
        print("cannot add, linked list is full")
    else:
        temp = startpointer
        startpointer = heappointer
        data[startpointer] = item
        heappointer = pointer[heappointer]
        pointer[startpointer] = temp

#search

def search(item):
    global data
    found = False
    for j in range(len(data)):
        if data[j] == item:
            found = True
            break

    if found:
        return j
    else:
        return False

#delete
    
def delete(item):
    global data, pointer, startpointer, heappointer
    global itempointer, olditempointer
    if startpointer == -1:
        print("cannot delete, linked list empty") 
        return 1
    else:
        itempointer = startpointer
        olditempointer = -1

        while itempointer != -1 and data[itempointer] != item:
            olditempointer = itempointer
            itempointer = pointer[itempointer]

        if itempointer == -1:
            print("item to be deleted not found")
            return 2

        if olditempointer == -1:
            startpointer = pointer[itempointer]
        else:
            pointer[olditempointer] = pointer[itempointer]

        pointer[itempointer] = heappointer
        heappointer = itempointer
        data[itempointer] = None

out()
add(9)
add(8)
add(7)
delete(8)
out()
