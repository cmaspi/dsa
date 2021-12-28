class linked_list:
    def __init__(self) -> None:
        self.head = None
    class node:
        def __init__(self, data) -> None:
            self.key = data
            self.next = None
    def append(self, key):
        if self.head == None:
            self.head = self.node(key)
        else :
            last = self.head
            while last.next:
                last = last.next
            last.next = self.node(key)
    def insert(self, key):
        first = self.node(key)
        first.next = self.head
        self.head = first
    def pop(self, key):
        if self.head.key == key:
            self.head = self.head.next
        else:
            last = self.head
            while last.next:
                if last.next.key == key:
                    last.next = last.next.next
                    return
                last = last.next
            raise ValueError("Key not found in the list")

    def print(self):
        last = self.head
        while last:
            print(last.key,end=" ")
            last = last.next
        print()
myList = linked_list()
myList.insert(2)
myList.append(3)
myList.print()
myList.insert(1)
myList.print()
myList.pop(1)
myList.pop(3)
myList.print()
myList.pop(2)
myList.print()



