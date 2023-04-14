# DFS 후위순위 (postorder)

def LCA(root, q, p):
    if root == None:
        return None
    
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if root == q or root == p:
        return root
    elif left and right:
        return root
    return left or right




def LCA(root, p, q):
    if root == None:
        return None
    
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if root == q or root == p:
        return root
    elif left and right:
        return root
    return left or right