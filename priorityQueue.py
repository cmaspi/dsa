'''
We would enter a key, priority pair. tasks with higher priority need to be done first

This implementation is using the binary heap data structure
Time complexity
insert log(n)
delete log(n)
getHighestPriority constant time
'''



class priorityQueue:
    def __init__(self) -> None:
        # self.queue = [{"key":1,"priority":4},{"key":2,"priority":9},{"key":3,"priority":3},{"key":4,"priority":10},{"key":5,"priority":1},{"key":6,"priority":5},{"key":7,"priority":2}]
        self.queue = []
    def swap(self, i, j):
        temp = self.queue[i]
        self.queue[i] = self.queue[j]
        self.queue[j] = temp
    
    def heapify(self, index):
        l = 2*index+1
        r = l+1
        if l>= len(self.queue):
            return
        elif l == len(self.queue)-1:
            if self.queue[l]["priority"]>self.queue[index]["priority"]:
                self.swap(l,index)
        else:
            largest = l if self.queue[l]["priority"]>self.queue[r]["priority"] else r
            if self.queue[largest]["priority"]>self.queue[index]["priority"]:
                self.swap(index,largest)
                self.heapify(largest)
    
    def upHeapify(self,index):
        parent = (index-1)//2
        if parent>=0:
            if self.queue[index]["priority"]>self.queue[parent]["priority"]:
                self.swap(index,parent)
                self.upHeapify(parent)
    

    
    def enqueue(self, key, priority):
        self.queue.append({"key":key,"priority":priority})
        self.upHeapify(len(self.queue)-1)
    
    def dequeue(self):
        root = self.queue[0]
        self.queue[0] = self.queue.pop()
        self.heapify(0)
        return root["key"]
    def getHighestPriority(self):
        return self.queue[0]["priority"]

    def prt(self):
        for i in range(len(self.queue)):
            print(self.queue[i]["priority"],end=" ")
        print()


a = priorityQueue()
a.enqueue(1,4)
a.enqueue(2,9)
a.enqueue(3,3)
a.enqueue(4,10)
a.enqueue(5,1)
a.enqueue(6,5)
a.enqueue(7,2)

print(a.getHighestPriority())

# a.heapify(0)
a.prt()
a.dequeue()
a.prt()

