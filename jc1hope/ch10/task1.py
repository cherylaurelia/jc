# Find the total of all elements in an array and the highest and lowest elements

import random
list = [random.randint(1,100) for _ in range(10)]
print(list)

lowest = 100
highest = 1
total = 0

for i in range (len(list)):
    total = total + list[i]
    if list[i] < lowest:
        lowest = list[i]
    elif list[i] > highest:
        highest = list[i]
    
print(f"The highest is {highest}, the lowest is {lowest} and the total is {total}")

