size = int(input())
new_list = [[] for _ in range(size)]

for i in range(size):
    num_edges = int(input())
    edges = []
    
    for _ in range(num_edges):
        s = int(input())
        d = int(input())
        edges.append((s, d))
    
    new_list[i] = edges

print(new_list)

visited = [False] * size  # Initialize visited list with False values
stack = []
stack.append(0)
while len(stack) != 0:
    current = stack.pop()
    
    if not visited[current]:
        print(current)
        visited[current] = True
        
        for edge in new_list[current]:
            xx = edge[1]
            if not visited[xx]:
                stack.append(xx)