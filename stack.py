# This is the python code for implementation of the stack data structure,
# we need the following functions
# 1) push
# 2) pop
# 3) length
# 4) top

class __stack__:
    def __init__(self, capacity) -> None:
        self.stack = []
        self.capacity = capacity
    def push(self, element):
        if len(self.stack)==self.capacity:
            raise MemoryError("Stack is full")
        else:
            self.stack.append(element)
    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("The stack is empty")
        else :
            self.stack.pop(len(self.stack)-1)
    def length(self):
        return len(self.stack)
    def top(self):
        return self.stack.pop(len(self.stack)-1)

myStack = __stack__(5)
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.pop()
print(myStack.top())

