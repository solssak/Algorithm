# BFS (너비 우선 탐색)

def bfs(root):
    visited = [] # 그래프에서는 필수, level order는 방문 순서 표시 용도
    if root is None:
        return 0
    q = deque()
    q.append(root)
    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

bfs(root)




