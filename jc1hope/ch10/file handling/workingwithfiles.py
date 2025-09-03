#OPENFILE "names.txt" FOR READ
# print(file) io.textiowrapper name = "names.txt" mode= 'r' encoding = 'cp1252'
# print(file.read) built in method read of _io.TextIOWrapper object at 0x
# print(file.read()) normal
# print(file.read(1)) first character
# print(file.readline()) first line
#for line in file also works, prints every line with newline

# file = open("names.txt", 'a')
# file.write("hehe\n")
# file.close()

# try:
#     )file = open("names.txt",'r')
#     for i in file:
#         print(i.strip()) #print(i, end="") but not as effective
# except FileNotFoundError:
#     print("File not found")
# finally:
    # file.close(

#name = "     cheryl     "
#print(name.lstrip()) #strip left side 

# Names = []
# file = open("names.txt",'r')
# for line in file:
#     Names.append(line)

# print(Names)

# Write a programme to initialize an array of size 5 with values apple orange guava grapes banana 
#copy contents of array to the files by name fruits.txt
#output contents

fruits = ["apple", "orange","guava","grapes","banana"]

file = open("fruits.txt",'a')
for i in range(len(fruits)):
    file.write(f"{fruits[i]} \n")

file.close()

file = open("fruits.txt",'r')
print(file.read())
    
def DeleteComment(stringline):
 endofline = stringline[-1]
 for i in range(len(stringline)):
    if stringline[i] and stringline[i+1] == "/":
       lengthofcomment = len(stringline[i:])
       for j in range(len(stringline)- lengthofcomment):
            stringline[j] = stringline[i]
       
