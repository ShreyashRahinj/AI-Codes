from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]

def bfs(source,target,n):
    visited = [False]*n
    pq = PriorityQueue()

    pq.put((0,source))
    visited[source] = True
    totalCost = 0

    while not pq.empty():
        
        cost , minimumNode = pq.get()
        print(minimumNode,end=' ')
        totalCost += cost

        if(minimumNode == target):
            print()
            print(totalCost)
            break

        for v,c in graph[minimumNode]:
            if not visited[v]:
                visited[v] = True
                pq.put((c,v))

def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
 
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)
 
source = 0
target = 9
bfs(source, target, v)