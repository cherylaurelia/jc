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

def reverseString(str):
    if len(str) == 1:
        return str
    else:
        return 0 #uh


    
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

        
        
