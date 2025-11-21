#a 

class Picture:
    def __init__(self, pDesc, pWidth, pHeight, pFrameColor):
        self.__desc = pDesc #str
        self.__width = pWidth #int
        self.__height = pHeight #int
        self.__framecolor = pFrameColor #str
    
    #b
    def GetDescription(self):
        return self.__desc
    
    def GetWidth(self):
        return self.__width
    
    def GetHeight(self):
        return self.__height
    
    def GetFrameColor(self):
        return self.__framecolor
    
    #c
    def SetDescription(self, newdesc):
        self.__desc = newdesc

#d

arrayPicture = [] #array of size 100 of type Picture

#e

def ReadData():
    try:
        file = open("jc2hope/Pictures.txt", 'r')
        line = file.readline().strip()
        while line != "":
            desc = line
            width = int(file.readline().strip())
            height = int(file.readline().strip())
            framecolor = file.readline().strip()
            arrayPicture.append(Picture(desc, width, height, framecolor))
            line = file.readline().strip()
        return(len(arrayPicture))
    except FileNotFoundError as e:
        print(f"File not found! {e}")

#f

ReadData()

#g 

usercolorframe = str(input("Enter a frame color: "))
usermaxwidth = int(input("Enter a max width: "))
usermaxheight = int(input("Enter a max height: "))

for i in range(len(arrayPicture)):
    if arrayPicture[i].GetFrameColor().lower() == usercolorframe.lower():
        if arrayPicture[i].GetWidth() <= usermaxwidth:
            if arrayPicture[i].GetHeight() <= usermaxheight:
                print(arrayPicture[i].GetDescription(), arrayPicture[i].GetWidth(), arrayPicture[i].GetHeight(), arrayPicture[i].GetFrameColor())