class Graph:
    def __init__(self, num):
        self.num = num
        self.graph = [None]*self.num
    class node:
        def __init__(self, key) -> None:
            self.key = key
            self.next = None
    
    # this is for undirected graph
    def add_edge(self, src, dest):
        temp = self.node(dest)
        temp.next = self.graph[src]
        self.graph[src] = temp
        if src != dest:
            temp = self.node(src)
            temp.next = self.graph[dest]
            self.graph[dest] = temp
    
    def BFS(self, index):
        queue = []
        visited = [False]*self.num
        visited[index] = True
        queue.append(index)
        while queue:
            print(queue[0],end=' ')
            s = queue.pop(0)
            s = self.graph[s]
            while s:
                if not visited[s.key]:
                    queue.append(s.key)
                    visited[s.key] = True
                s= s.next
    
    def BFS_min_edges(self, u, v):
        distance = [0]*self.num
        queue = []
        visited = [False]*self.num
        queue.append(u)
        while queue:
            s = queue.pop(0)
            dist = distance[s]
            if s == v:
                return dist
            s = self.graph[s]
            while s:
                if not visited[s.key]:
                    queue.append(s.key)
                    distance[s.key] = dist+1
                    visited[s.key] = True
                s = s.next



    def DFS_util(self, index,visited=None):
        if visited is None:
            visited = [False]*self.num

        visited[index] = True
        print(index,end = " ")
        s = self.graph[index]
        while s:
            if not visited[s.key]:
                visited = self.DFS_util(s.key,visited)
            s = s.next
        return visited
    def DFS(self,index):
        self.DFS_util(index)
        print()




    def display(self):
        for i in range(self.num):
            print('src: {}'.format(i))
            temp = self.graph[i]
            while temp:
                print(" ->",temp.key,end="")
                temp = temp.next
            print()


mygraph = Graph(7)
mygraph.add_edge(0,1)
mygraph.add_edge(0,2)
mygraph.add_edge(0,4)
mygraph.add_edge(1,2)
mygraph.add_edge(2,5)
mygraph.add_edge(3,4)
mygraph.add_edge(4,5)
mygraph.add_edge(4,6)
# mygraph.display()
# mygraph.DFS(1)
print(mygraph.BFS_min_edges(1,6))
# print(mygraph.graph[2].key)