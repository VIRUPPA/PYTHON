def unique_grid(m,n):
    dp = []
    for _ in range(m):
        row = []
        for _ in range(n):
            row.append(0)
        dp.append(row)

    for i in range(m):
        dp[0][i] = 1
    for j in range(n):
        dp[j][0] = 1

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    for row in dp:
        print(row)

    return dp[m-1][n -1]

total = unique_grid(4,4)
print(total)
