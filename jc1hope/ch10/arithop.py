num1 = 5 #num is of type int
num2 = 2
sum = num1 + num2 
diff = num1 - num2
prod = num1 * num2
quot = num1 / num2
int_quot = num1 // num2 #int_quot <- num1 DIV num2
rem = num1 % num2 #rem <- num1 MOD num2

print(f"Sum is {sum}")
print(f"Difference is {diff}")
print(f"Product is {prod}")
print(f"Quotient is {quot}")
print(f"Integer quotient is {int_quot}")
print(f"Remainder is {rem}")

myArr = [0]*10 #array of len 10

print(myArr)

for index in range(10):
    print(myArr[index])

for element in myArr:
    print(element)
