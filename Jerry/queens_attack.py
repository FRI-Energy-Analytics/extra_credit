def branch(dR, dC, n, r_q, c_q, obstacles):
    res = 0

    curr_row = r_q + dR
    curr_col = c_q + dC
    
    while 1 <= curr_row <= n and 1 <= curr_col <= n and (curr_row, curr_col) not in obstacles:
        curr_row += dR
        curr_col += dC
        res += 1

    return res
    
def queensAttack(n, k, r_q, c_q, obstacles):
    res = 0

    obstacles_set = set((obstacles[i][0], obstacles[i][1]) for i in range(len(obstacles)))

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not i == 0 or not j == 0:
                res += branch(i, j, n, r_q, c_q, obstacles_set)

    return res
