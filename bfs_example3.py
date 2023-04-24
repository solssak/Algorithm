# 1번 - return 값과 경로 없을 때 값 설정 (-1)
# 2번 - 가로(col), 세로(row) 설정
# 3번 - queue 설정
# 4번 - 방문 표시. 2차원 matrix 모두 false로 생성
# 5번 - 현재값 설정 cur_c, cur_r, cur_len
# 6번 - 좌표 설정 delta = [(), (), (), ...], 연결되어있는 vertex 확인
# 7번 - row, col 범위 설정, 0일 때 가지 말고, 방문했던 곳 가지 마라
# 8번 - 방문할 곳 정해주고 방문표시 해주기
# 9번 - 목적지에 도착했을 때 cur_len shorest_path_len 에 저장해주기
# ---------------------------
# 10번 - 예외 처리

from collections import deque

def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1
    row = len(grid)
    col = len(grid[0])

    visited = [[False]*col for _ in range(row)]

    delta = [(1,0), (-1,0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True

    while queue:
        cur_r, cur_c, cur_len = queue.popleft()
        # if cur_c - 1 == 0 and cur_r - 1 == 0:
        if cur_r == row -1 and cur_c == col - 1:
            shortest_path_len = cur_len
            break

        for dr, dc in delta:                                                      # 6번 - 연결되어있는 vertex 확인하기
            next_r = cur_r + dr                                                   # 6번 - 연결되어있는 vertex 확인하기
            next_c = cur_c + dc                                                   # 6번 - 연결되어있는 vertex 확인하기
            if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:  # 7번 - row, col 범위 안 지정
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:  # 7번 - 0일 때, 방문했던 곳 가지 마라
                    queue.append((next_r, next_c, cur_len + 1))  # 8번 - queue에 방문할 곳 정해줌
                    visited[next_r][next_c] = True               



    return shortest_path_len

grid = [[0,0,0],[1,1,0],[1,1,0]] 
print(shortestPathBinaryMatrix(grid))
