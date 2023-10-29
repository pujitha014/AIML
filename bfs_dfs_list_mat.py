def adj_list():
    size = int(input("Enter the number of nodes: "))
    new_list = [[] for _ in range(size)]

    for i in range(size):
        num_edges = int(input(f"No of edges for the node {i}:"))
        edges = []
        
        for _ in range(num_edges):
            d = int(input(f"Enter the destination node for node {i}: "))  
            edges.append(d)
            
        new_list[i] = edges
    
    return new_list  

def adj_matrix():
    size = int(input("Enter the number of nodes: "))
    adj_matrix = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        num_edges = int(input(f"Enter the number of edges for node {i}: "))
        
        for _ in range(num_edges):
            dest = int(input(f"Enter the destination node for node {i}: "))
            adj_matrix[i][dest] = 1

    return adj_matrix  

def bfs(new_list, size):
    visited = [False] * size
    queue = []
    queue.append(0)
    
    while queue:
        current = queue.pop(0)
        
        if not visited[current]:
            print("Visited node:", current)
            visited[current] = True
            for neighbor in new_list[current]:
                if not visited[neighbor]:
                    queue.append(neighbor)

def dfs(new_list, size):
    visited = [False] * size
    stack = []
    stack.append(0)  

    while stack:
        current = stack.pop()

        if not visited[current]:
            print("Visited node:", current)
            visited[current] = True
            for neighbor in new_list[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)

def main():
    while True:
        print("Enter the choice")
        print("1.adjacency matrix 2.adjacency list 3.exit")
        ch = int(input())
        
        if ch == 1:
            new_matrix = adj_matrix()  
            size_matrix = len(new_matrix)
            for i in new_matrix:
                print(i)

            # print(new_matrix)
            print("Enter the choice")
            print("B.BFS D.DFS T.BOTH X.Exit")
            ch1 = input()
            if ch1 == 'B':
                print("BFS-")
                bfs(new_matrix, size_matrix)
            elif ch1 == 'D':
                print("DFS-")
                dfs(new_matrix, size_matrix)
            elif ch1 == 'T':
                print("BFS-")
                bfs(new_matrix, size_matrix)
                print("DFS-")
                dfs(new_matrix, size_matrix)
            elif ch1 == 'X':
                exit()
            else:
                print("Enter the correct choice")

        elif ch == 2:
            new_list = adj_list()
            size_list = len(new_list)
            print("Enter the choice")
            print("b.BFS d.DFS t.BOTH x.Exit")
            ch1 = input()
            if ch1 == 'b':
                print("BFS-")
                bfs(new_list, size_list)
            elif ch1 == 'd':
                print("DFS-")
                dfs(new_list, size_list)
            elif ch1 == 't':
                print("BFS-")
                bfs(new_list, size_list)
                print("DFS-")
                dfs(new_list, size_list)
            elif ch1 == 'x':
                exit()
            else:
                print("Enter the correct choice")
        elif ch==3:
            exit()
        else:
            print("Enter the correct choice")


if __name__ == "__main__":
    main()
