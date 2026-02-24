#Q1

#a)

def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        

#Q2 

#a)

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
        
#Q3

#a)

def countdown(n):
    if n == 1:
        print(n)
        print("Done")
    else:
        print(n)
        return(countdown(n-1))
        
        
#Q4

#a)

def reverseString(s):
    if s == "":
        return ""

    return reverseString(s[1:]) + s[0]


    
#Q5

#a)

def power(base, exp):
    if exp == 0:
        return 1 
    else:
        return (base * power(base, exp -1))
        
#Q6

#a)

def countDigits(n):
    if n < 10:
        return 1
    return 1 + countDigits(n // 10)

#Q7

#a)

def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)


#Q8

#a)

def sumOfArray(arr):
    if len(arr) == 0:
        return 0

    return arr[0] + sumOfArray(arr[1:])

#Q9

#a)

def binarysearch(arr, se, lb, ub):
    if low > high:
        return -1

    mid = (lb + ub) // 2

    if arr[mid] == se:
        return mid
    elif se < arr[mid]:
        return binarySearch(arr, se, lb, mid - 1)
    else:
        return binarySearch(arr, se, mid + 1, ub)

#Q10

#a)

def hanoi(n, source, auxiliary, target):
    return 1
        
        

