#Q1

def Unknown(x,y):
    if x < y:
        print(x+y)
        return (Unknown(x+1, y) * 2)
    elif x == y:
        return 1 
    else:
        print(x+y)
        return(Unknown(x-1, y) // 2)
        
Unknown(10,15)
Unknown(10,10)
Unknown(15,10)


#Q3

ArrayNodes = [[None for row in range(3)] for col in range (20)]
RootPointer = -1
FreeNode = 0 

def AddNode():
    global ArrayNodes, RootPointer, FreeNode
    NodeData = int(input("Enter the data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode,0] = -1
        ArrayNodes[FreeNode,1] = NodeData
        ArrayNodes[FreeNode,2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False 
            CurrentNode = RootPointer
            while not Placed:
                if NodeData < ArrayNodes[CurrentNode,1]:
                    if ArrayNodes[CurrentNode, 0] == -1:
                        ArrayNodes[CurrentNode, 0] = FreeNode
                        Placed = True 
                    else:
                        CurrentNode = ArrayNodes[CurrentNode, 0]
                else:
                    if ArrayNodes[CurrentNode,2] = -1:
                        ArrayNodes[CurrentNode,2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode,2]
            
        
        FreeNode = FreeNode + 1
     else:
         print("tree is full")
        
            
                    
    
