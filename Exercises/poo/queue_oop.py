class Queue:
    def __init__(self):
        self.items = []
    
    def enQueue(self, item) -> None:
        self.items.append(item)

    def deQueue(self) -> None:
        self.items.pop(0)

    def viewSize(self) -> list:
        return len(self.items)
    
    def isEmpty(self) -> bool:
        return len(self.items) == 0

def main() -> None:
    queue = Queue()

    queue.enQueue(3)
    queue.enQueue(7)
    queue.enQueue(0)

    print(queue.viewSize())
    print(queue.isEmpty())

main()