def LCA(root, p, q):
    if root == None:
        return None
    
    left = LCA(root, p, q)
    right = LCA(root, p, q)
    if root == p or root == q:
        return root
    elif left and right:
        return root
    return left or right