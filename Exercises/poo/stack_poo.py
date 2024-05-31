#This code represent a stack, that works based on FIFO paradigm, in python with poo

class Stack:
    def __init__(self, items):
        self.items = items

    def pushing(self, data) -> None:
        self.data = data
        self.items.append(data)

    def popping(self) -> None:
        self.items.pop()

    def viewdata(self):
        return self.items
    
    def viewpeek(self) -> int:
        return self.items[len(self.items)-1]
    
    def isempty(self) -> bool:
        return len(self.items) == 0
    
    def viewsize(self):
        count = 0
        while True:
            if (self.items[count] != self.items[-1]):
                count += 1
                continue
            else:
                count += 1
                break
        
        return count

def main() -> None:
    stack1 = Stack(['1', 2, 'hello', 'append', 'stack'])

    print(f"\n{stack1.viewdata()}")
    stack1.popping()
    print(stack1.viewsize())
    print(stack1.isempty())

    print("\n====================================\n")

    stack2 = Stack(['dunno', 'ball', 1.34])
    print(stack2.viewdata())
    print(stack2.viewsize())

main()