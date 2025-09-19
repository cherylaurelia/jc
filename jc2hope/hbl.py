# task 1

class Book:
    def __init__(self, pTitle, pAuthor, pisBorrowed):
        self.__title = pTitle
        self.__author = pAuthor
        self.__isBorrowed = pisBorrowed

    def getTitle(self):
        return self.__title
    
    def getAuthor(self):
        return self.__author
    
    def getisBorrowed(self):
        return self.__isBorrowed
    
    def setTitle(self, new):
        self.__title = new

    def setAuthor(self, new):
        self.__author = new
    
    def setisBorrowed(self, new):
        self.__isBorrowed = new

    def borrowBook(self):
        self.__isBorrowed = True

    def returnBook(self):
        self.__isBorrowed = False

    def getStatus(self):
        return(f"Title : {self.__title}, Author: {self.__author}, Borrowed: {self.__isBorrowed}")
    

bookArr = []

book1 = Book("Book1", "Author1", True)
book2 = Book("Book2", "Author2", True)
book3 = Book("Book3", "Author3", False)
book4 = Book("Book4", "Author4", False)

bookArr.append(book1)
bookArr.append(book2)
bookArr.append(book3)
bookArr.append(book4)

book4.borrowBook()
print(book4.getStatus())
book4.returnBook()
print(book4.getStatus())

#task 2

class Employee:
    def __init__(self, pempID, pempName, pSalary):
        self.__empID = pempID
        self.__empName = pempName
        self.__salary = pSalary

    def getempID(self):
        return self.__empID
    
    def getempName(self):
        return self.__empName
    
    def getSalary(self):
        return self.__salary
    
    def setempID(self, new):
        self.__empID = new
    
    def setempName(self, new):
        self.__empName = new

    def setSalary(self, new):
        self.__salary = new

    def showDetails(self):
        return(f"Employee ID: {self.__empID}\nEmployee Name: {self.__empName}\nSalary: {self.__salary}")
    
    def increaseSalary(self, percentage):
        self.__salary = self.__salary * (1 + (percentage/100))

employee1 = Employee("123", "Name1", 12000.0)
employee2 = Employee("12", "Name2", 2000.0)
employee3 = Employee("13", "Name3", 1000.0)
employee4 = Employee("124", "Name4", 120000.0)

employeeArr = []

employeeArr.append(employee1)
employeeArr.append(employee2)
employeeArr.append(employee3)
employeeArr.append(employee4)

print(employee1.showDetails())

for employee in employeeArr:
    employee.increaseSalary(30.0)

print(employee1.showDetails())

#task 3

class Item:

    def __init__(self, pName, pPrice):
        self.__name = pName
        self.__price = pPrice

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def setName(self, newname):
        self.__name = newname

    def setPrice(self, newprice):
        self.__price = newprice

    def itemDetails(self):
        return(f"Name: {self.__name}\nPrice: {self.__price}")


class Cart:

        def __init__(self):
            self.cartArr = []

        def addItem(self, newitem):
            self.cartArr.append(newitem)

        def showCartDetails(self):
            for item in self.cartArr:
                print(f"Item Name: {item.getName()}\nItem Price: {item.getPrice()}\n\n")

        def calculateTotal(self):
            total = 0
            for item in self.cartArr:
                total += item.getPrice()
            print(total)



item1 = Item("carrot", 15)
item2 = Item("book", 20)
item3 = Item("tree", 1000)
item4 = Item("toilet", 2)

cart1 = Cart()

cart1.addItem(item1)
cart1.addItem(item2)
cart1.addItem(item3)
cart1.addItem(item4)

cart1.showCartDetails()
cart1.calculateTotal()

#task 4

class Passenger:
    def __init__(self, pName, ppassportNumber):
        self.__name = pName
        self.__passportnumber = ppassportNumber

    def getName(self):
        return self.__name
    
    def getpassportNumber(self):
        return self.__passportnumber
    
    def setName(self,new):
        self.__name = new

    def setpassportNumber(self,new):
        self.___passportnumber = new

    def passengerDetails(self):
        return(f"Name: {self.__name}\nPassport Number: {self.___passportnumber}")
    
class Flight:
    def __init__(self):
        self.flightArr = []

    def addPassenger(self, newPassenger):
        self.flightArr.append(newPassenger)

    def displayPassengers(self):
        for passenger in self.flightArr:
                print(f"Passenger Name: {passenger.getName()}\nPassenger Passport Number: {passenger.getpassportNumber()}\n\n")

passenger1 = Passenger("name1", "1")
passenger2 = Passenger("name2", "2")
passenger3 = Passenger("name3", "3")
passenger4 = Passenger("name4", "4")

flight1 = Flight()

flight1.addPassenger(passenger1)
flight1.addPassenger(passenger2)
flight1.addPassenger(passenger3)
flight1.addPassenger(passenger4)

flight1.displayPassengers()