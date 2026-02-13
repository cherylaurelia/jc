#3 a) i) ii) iii)

class Node:
    #i)
    def __init__(self, TheData):
        self.__data = TheData #integer
        self.__nextnode = None #Node

    #ii)
    def GetData(self):
        return self.__data
    
    def GetNextNode(self):
        return self.__nextnode
    
    #iii)
    def SetNextNode(self, new):
        self.__nextnode = new

#3 b) i) ii) iii)
        
class LinkedList:
    #i)
    def __init__(self):
        self.__headnode = None #Node

    #ii)
    def InsertNode(self, new):
        newnode = Node(new)
        newnode.SetNextNode(self.__headnode)
        self.__headnode = newnode

    #iii)
    def Traverse(self):
        string = ""
        currentnode = self.__headnode
        while currentnode != None:
            string += str(currentnode.GetData()) + " "
            currentnode = currentnode.GetNextNode()
        return string
    
    #iv)
    def RemoveNode(self, item):
        if self.__headnode == None:
            print("linked list is empty")
            return False
        
        if self.__headnode.GetData() == item:
            self.__headnode = self.__headnode.GetNextNode()
            return True
        
        found = False
        currentnode = self.__headnode
        while not found and currentnode != None:
            if ((currentnode).GetNextNode()).GetData() == item:
                currentnode.SetNextNode(currentnode.GetNextNode().GetNextNode())
                found = True
            else:
                currentnode = currentnode.GetNextNode()

#3 c) i) 
                
LL = LinkedList()
LL.InsertNode(10)
LL.InsertNode(20)
LL.InsertNode(30)
LL.InsertNode(40)
LL.InsertNode(50)

print(LL.Traverse())
LL.RemoveNode(30)
print(LL.Traverse())