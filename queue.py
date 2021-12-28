"""
This is the code for queue data structure
The following functions are available
1) enqueue
2) dequeue
3) is_empty
"""
class __queue__:
    def __init__(self, capacity) -> None:
        self.queue = [None for _ in range(capacity)]
        self.capacity = capacity
        self.front = None
        self.rear = None
    
    def enqueue(self,element):
        if self.front is None:
            self.front = 0
            self.rear = -1
        if self.rear == (self.front-1)%self.capacity:
            raise MemoryError("Queue is full")
        else:
            self.rear = (self.rear+1)%self.capacity
            self.queue[self.rear] = element

    def dequeue(self):
        if self.front is None:
            raise IndexError("The queue is already empty")
        else :
            # self.queue[self.front]
            if self.front == self.rear:
                self.front = None
            else:
                self.front = (self.front+1)%self.capacity


    def prt(self):
        if self.front is None:
            return []

        elif self.front <= self.rear:
            print(self.queue[self.front : self.rear+1])
        else:
            print(self.queue[self.front:]+self.queue[:self.rear+1])


myQueue = __queue__(4)
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.dequeue()
# myQueue.dequeue()
myQueue.dequeue()
myQueue.prt()
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
# myQueue.enqueue(6)
myQueue.prt()




