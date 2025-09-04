# class Shape:
#     pass

# shape1 = Shape()
# print(shape1)

#stub module

class Shape:
    def __init__(self, Plen, Pheight):
        self.len =  Plen 
        self.height = Pheight

    def area(self):
        return self.len * self.height
    
shape1 = Shape(2,4)

# print(shape1, shape1.len, shape1.height, shape1.area())

hoursworked = 5
overtime = 6
allowance = 8

class Employee:
    def __init__(self, name, gender, pay):
        self.name = name
        self.gender = gender
        self.pay = pay

    def calculate_salary(self):
        return ((hoursworked * self.pay) + (overtime * allowance))

employee1 = Employee("cait","male",4000)

print(employee1.name, employee1.gender, employee1.pay, employee1.calculate_salary())