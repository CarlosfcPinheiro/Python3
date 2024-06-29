class Item:
    def __init__(self, value1=1, value2=1):
        self.__value1 = value1
        self.value2 = value2

    @property
    def value1(self):
        return self.__value1

    @value1.setter
    def value1(self, newvalue1):
        self.__value1 = newvalue1

    def sumValues(self):
        return self.__value1 + self.value2
    
item = Item(2, 2)

print(item.sumValues())

num = 5
print(f"num + __value1 = {num + item.value1}")

item.value1 = 3
print(item.sumValues())
    



