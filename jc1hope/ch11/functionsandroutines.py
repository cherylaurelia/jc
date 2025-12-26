#subroutines combined together will do main task
#modular/structured program
# it achieves reusability
# it can reduce errors *
# differentiate between procedures and functions (1. 2. 3. )

# 1. a procedure is a subroutine which performs the task it was intended to perform but does not return any value back to the calling program.  a function is a subroutine which performs the task it was intended to perform and returns any value back to the calling program
# 2. a procedure call is a statement while a function call is an expression or part of the expression
# 3. 

# PROCEDURE <identifier> () // PROCEDURE header
#     body of the procedure
# END PROCEDURE

# PROCEDURE <identifier> (param1, param2) // PROCEDURE header
#     body of the procedure
# END PROCEDURE

# a parameter is a value that a function or a procedure takes
# a parameter is declared in the function or procedure header

# PROCEDURE PrintMyName()
#   OUTPUT "cheryl"
# ENDPROCEDURE

# to call a procedure - statement
# CALL PrintMyName()

# def output():
#     print("olelale")

# output()

# def Print(name):
#     print(name)

# Print("eong")

# differentiate between parameter and argument. argument is "eong" and parameter is name. parameter receives the value of the argument
# in pseudocode, data type is very important while for python its not. pseudocode needs declaration

# PROCDURE PrintMyName(name: STRING , age:INTEGER)
#   OUTPUT "my name lelolelo"
# ENDPROCEDURE

#arguments can be passed to procedure in two ways
# 1. pass by value - BYVAL by default. 
# 2. pass by reference - BYREF // BYREF num 1, must specify BYVAL num 2. num 1, BYREF num 2 dont need specify

#PROCEDURE SqrOfNum(BYVAL num1: INTEGER, num2: INTEGER)
    #OUTPUT "The square of the number is", num * num
#ENDPROCEDURE

#PROCEDURE SqrOfNum(num: INTEGER)
    #num <- num * num
    #OUTPUT "num inside procedure is", num // 16
#ENDPROCEDURE

#num <- 4
#OUTPUT "num outside before the procedure is called", num // 4
#CALL SqrOfNum(num)
#OUTPUT "num outside after the procedure is called", num // 4. why not 16? bcs num and num in procedure is diff. num in procedure is local variable, scope limited to only inside procedure
# BUT the above is only for BYVA, new var with same name. if u use BYREF, it "refers" to the same variable at the same memory location, it will become 16 instead.
# never pass value byref to a function in pseudocode. why? bcs


#in python, all values are passed as objects by reference. 
# a variable can be mutable (can change) and immutable (cannot change)???
# if u pass a mutable var, it will pass by value
# if u pass immutable, it will pass by reference

# myNum = 5
# myList = [0,1,2,3]

# def passbyvalue(myNum):
#     myNum = myNum * myNum
#     print(f"during: {myNum}")

# def passbyref(myList):
#     myList[0] = 4
#     myList[1] = 5
#     print(f"during: {myList}")

# print(f"before: {myNum}")
# passbyvalue(myNum)
# print(f"after: {myNum}")

# print(f"before: {myList}")
# passbyref(myList)
# print(f"after: {myList}")

# FUNCTION <identifier> RETURNS <data type> 
#   body of function
#   RETURN <identifier> // always last statement. both pseudo and py
# ENDFUNCTION

# if you want to return multiple values, use an array (same data type)
# py can still have 2 diff data types, bcs it uses list NOT array

# FUNCTION SqrofNum(BYVAL myNum: INTEGER) RETURNS INTEGER //func always byval anyway
#   Sqr = myNum * myNum
#   RETURN Sqr
# ENDFUNCTION h


#Sqr <- SqrofNum(4) // sqr is now 16

# def sqrnum(num):
#     sqr = num * num
#     return sqr

# number = 4
# print(f"The square of {number} is {sqrnum(number)}")
