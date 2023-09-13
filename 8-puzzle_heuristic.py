import numpy as np

def create(matrix, c, d, r):
    def find():
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == 0:
                    c, d = i, j
        return c, d

    def left(matrix, c, d):
        if d > 0:
            matrix1 = np.copy(matrix)
            temp1 = matrix1[c][d - 1]
            matrix1[c][d - 1] = matrix1[c][d]
            matrix1[c][d] = temp1
            c, d = find()
            h_value = calculate_heuristic(matrix1)
            print(f"Level {r}, Heuristic: {h_value}\n{matrix1}")
            return matrix1, c, d

    def right(matrix, c, d):
        if d < 2:
            matrix1 = np.copy(matrix)
            temp1 = matrix1[c][d + 1]
            matrix1[c][d + 1] = matrix1[c][d]
            matrix1[c][d] = temp1
            c, d = find()
            h_value = calculate_heuristic(matrix1)
            print(f"Level {r}, Heuristic: {h_value}\n{matrix1}")
            return matrix1, c, d

    def up(matrix, c, d):
        if c > 0:
            matrix1 = np.copy(matrix)
            temp1 = matrix1[c - 1][d]
            matrix1[c - 1][d] = matrix1[c][d]
            matrix1[c][d] = temp1
            c, d = find()
            h_value = calculate_heuristic(matrix1)
            print(f"Level {r}, Heuristic: {h_value}\n{matrix1}")
            return matrix1, c, d

    def down(matrix, c, d):
        if c < 2:
            matrix1 = np.copy(matrix)
            temp1 = matrix1[c + 1][d]
            matrix1[c + 1][d] = matrix1[c][d]
            matrix1[c][d] = temp1
            c, d = find()
            h_value = calculate_heuristic(matrix1)
            print(f"Level {r}, Heuristic: {h_value}\n{matrix1}")
            return matrix1, c, d

    def calculate_heuristic(state):
        heuristic = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != goal_state[i][j]:
                    heuristic += 1
        return heuristic

    while not np.array_equal(matrix, goal_state):
        c, d = find()
        h_value = calculate_heuristic(matrix)
        print(f"Level {r}, Heuristic: {h_value}\n{matrix}")

        result = left(matrix, c, d)
        if result is not None:
            matrix, c, d = result
        else:
            
            result = right(matrix, c, d)
            if result is not None:
                matrix, c, d = result
            else:
                result = up(matrix, c, d)
                if result is not None:
                    matrix, c, d = result
                else:
                    result = down(matrix, c, d)
                    if result is not None:
                        matrix, c, d = result

        r += 1

    if np.array_equal(matrix, goal_state):
        print("Solution found")
    else:
        print("No solution found")

print("Enter the start state")
matrix = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

c, d = 0, 0
r = 0
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] 
create(np.array(matrix), c, d, r)
