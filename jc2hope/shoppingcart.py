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


class Cart:

        def __init__(self):
            self.cartArr = []

        def calculateTotal(self):
            return sum(cart.Arr.

        def addItem(self, newitem):
            self.cartArr.append(newitem)




item1 = Item("carrot", 15)
item2 = Item("book", 20)
item3 = Item("tree", 1000)
item4 = Item("toilet", 2)

cart1 = Cart()

cart1.addItem(item1)


