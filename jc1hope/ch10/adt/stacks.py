
#stack = [None for _ in range(10)] lifo 

stack = [1,2,3,4]
basePointer = 0
TopPointer = 2
Full = 3

def pop():
    global TopPointer
    if TopPointer == -1:
        print("Stack is empty, cannot pop")
    else:
        print(stack[TopPointer])
        TopPointer -= 1

def push(Element):
    global TopPointer, Full
    if TopPointer == Full:
        print("Stack is full, cannot push")
    else:
        TopPointer += 1
        stack[TopPointer] = Element

print(stack)
Element = int(input("Enter element to be pushed: "))
push(Element)
pop()
pop()
pop()
pop()
pop()