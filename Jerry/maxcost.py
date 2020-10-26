# Tries every single possible path
def backtrack(matrix, row, col, curr_cost):

    if not 0 <= row < len(matrix) or not 0 <= col < len(matrix[0]) or matrix[row][col] < 0:
        return 0

    if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
        return curr_cost + matrix[row][col]

    curr_max = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 or j == 0:
                curr_cell = matrix[row][col]
                matrix[row][col] *= -1
                curr_max = max(backtrack(matrix, row + i, col + j, curr_cell + curr_cost), curr_max)
                matrix[row][col] *= -1

    return curr_max

# Always goes to next greatest neighbor
def greedy(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    curr_pos = (0, 0)
    curr_cost = 0

    while curr_pos != (rows - 1, cols - 1):
        best_dir = (0, 0)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 or j == 0) and i != j:
                    curr_row = curr_pos[0]
                    curr_col = curr_pos[1]
                    if 0 <= curr_row + i < rows and 0 <= curr_col + j < cols:
                        if best_dir == (0, 0):
                            best_dir = (i, j)
                        else:
                            if matrix[curr_row + i][curr_col + j] > matrix[curr_row + best_dir[0]][curr_col + best_dir[1]]:
                                best_dir = (i, j)
        curr_cost += matrix[curr_pos[0]][curr_pos[1]]
        matrix[curr_pos[0]][curr_pos[1]] *= -1
        curr_pos = (curr_pos[0] + best_dir[0], curr_pos[1] + best_dir[1])

    return curr_cost + matrix[rows - 1][cols - 1]

# Tests/Observations

matrix = [
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]
        ]
# Snakes around matrix, hitting every number.
# Results in 45
print(backtrack(matrix, 0, 0, 0))

# Goes all the way down, then all the way to right.
# Results in 29
print(greedy(matrix))

greedy_breaker = [
                    [6, 1, 2], 
                    [5, 4, 3], 
                    [1, 1, 1]
                ]
# Backtracking can solve this without a problem
# Results in 24
print(backtrack(greedy_breaker, 0, 0, 0))

# Greedy algorithm keeps following the greatest neighbor into a "trap" (i.e. matrix[0][1])
# Where all neighbors have been visited and the end is not reached
# We would need to incorporate some backtracking mechanism to fix this problem
# Results in infinite loop
print(greedy(greedy_breaker))
