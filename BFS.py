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
queue = []
queue.append(0)
while len(queue) != 0:
    current = queue.pop(0)  # Use pop(0) to remove the element from the beginning of the queue
    #if not visited[current]:
    if  visited[current]==False:
        print(current)
        visited[current] = True
        for i in range(len(new_list[current])):
            xx = new_list[current][i][1]
            queue.append(xx)