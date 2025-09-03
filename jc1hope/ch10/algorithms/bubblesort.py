import random
list = [random.randint(1,100) for _ in range(10)]
print(list)

swap = True
length = len(list)
while swap:
    swap = False
    for i in range (length - 1):
        if list[i] > list[i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
            swap = True
    length -= 1
print(list)
        
        
