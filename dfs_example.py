from collections import deque

def numIsland(grid):
    number_of_islands = 0
    row = len(grid)
    col = len(grid[0])
    visited = [[False]*col for _ in range(row)]

    def bfs(x, y):
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        visited[x][y] = True
        queue = deque()
        queue.append((x, y))

        while queue:
            cur_x, cur_y = queue.popleft()
        
            for i in range(4):
                next_x =  cur_x + dx[i]
                next_y =  cur_y + dy[i]
        
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:           # m, n 범위 안
                    if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:     # 0이면 가지 말고 방문 안했으면 가라
        
                        visited[next_x][next_y] = True  # 위 조건을 통과해서 방문하면
                        queue.append((next_x, next_y))  # queue에 담아줌

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1" and not visited[i][j]:
                bfs(i, j)
                number_of_islands += 1
    return number_of_islands

print(numIsland(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])
)