# postorder

from collections import deque

def maxDepth(root):
    
    if root is None:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) +1