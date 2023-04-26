from collections import deque

def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1        # 1번 - 초기값 세팅
    row = len(grid)         # 2번 - 세로값 세팅
    col = len(grid[0])      # 2번 - 가로값 세팅

    if grid[0][0] != 0 or grid[row-1][col-1] != 0: # 10번 - 예외처리
        return shortest_path_len
    
    visited = [[False]*col for _ in range(row)]     # 4번 - 방문 표시

    delta = [(1,0), (-1,0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # 6번 - 좌표 설정

    queue = deque()               # 3번 - queue 세팅
    queue.append((0, 0, 1))       # 3번 - queue 세팅
    visited[0][0] = True                            # 4번 - 방문 표시

    while queue:
        cur_r, cur_c, cur_len = queue.popleft()         # 5번 - 현재 값 설정
        if cur_r == row - 1 and cur_c == col - 1: # 9번 - 목적지에 도착했을 때
            shortest_path_len = cur_len           # 9번 - 그때의 cur_len를 shortest_path_len에 저장하면 됨.
            break

        for dr, dc in delta:                                                      # 6번 - 연결되어있는 vertex 확인하기
            next_r = cur_r + dr                                                   # 6번 - 연결되어있는 vertex 확인하기
            next_c = cur_c + dc                                                   # 6번 - 연결되어있는 vertex 확인하기
            if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:  # 7번 - row, col 범위 안 지정
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:  # 7번 - 0일 때, 방문했던 곳 가지 마라
                    queue.append((next_r, next_c, cur_len + 1))  # 8번 - queue에 방문할 곳 정해줌
                    visited[next_r][next_c] = True               # 8번 - 방문 표시 해줌


    return shortest_path_len      # 1번 - return 값 설정

grid = [[0,0,0],[1,1,0],[1,1,0]] 
print(shortestPathBinaryMatrix(grid))
