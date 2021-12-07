# Input:
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
# Output: 1

# Input:
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
# Output: 3


def solution(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j >= len(grid[i]) or j < 0 or grid[i][j] != "1":
            return
        grid[i][j] = 0
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    answer = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                dfs(i, j)
                answer += 1
    print(answer)


solution(grid)
