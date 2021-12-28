class List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    class node:
        def __init__(self , val) -> None:
            self.key = val
            self.next = None
            self.previous = None
    def append(self, key):
        if self.head is None:
            self.head = self.node(key)
            self.tail = self.head
        else:
            self.tail.next = self.node(key)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
            
    def insert(self, key):
        first = self.node(key)
        first.next = self.head
        if self.head is None:
            self.head = first
            self.tail = first
        else:
            self.head.previous = first
            self.head = first
    def pop(self, key):
        if self.head.key == key:
            self.head = self.head.next
            if self.head:
                self.head.previous = None
        else:
            last = self.head
            while last.next:
                if last.next.key == key:
                    last.next = last.next.next
                    if last.next:
                        last.next.previous = last
                    else:
                        self.tail = last                    
                    return
                last = last.next
            raise ValueError("Key not found in the list")
    def print(self):
        last = self.head
        while last:
            print(last.key,end=" ")
            last = last.next
        print()
    def printInreverse(self):
        last = self.tail
        while last:
            print(last.key,end=' ')
            last = last.previous
        print()

myList = List()
myList.append(2)
myList.append(3)
myList.insert(1)
myList.printInreverse()
myList.pop(3)
myList.printInreverse()
