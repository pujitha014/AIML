size = int(input())
graph = [[] for _ in range(size)]

for i in range(size):
    num_edges = int(input())
    
    for _ in range(num_edges):
        s = int(input())
        d = int(input())
        graph[i].append((s, d))

visited = [False] * size  
stack = []  

def dfs(vertex):
    visited[vertex] = True
    
    for edge in graph[vertex]:
        neighbor = edge[1]
        if neighbor < 0 or neighbor >= size:
            continue  
        if not visited[neighbor]:
            dfs(neighbor)
    
    stack.append(vertex) 

def topsort():
    for i in range(size):
        if not visited[i]:
            dfs(i)
    while len(stack) != 0:
        print(stack.pop(), end=" ")

topsort()