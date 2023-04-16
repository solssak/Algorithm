class Solution(object):
    def lowestCommonAncestor(self, root, p, q): #root 를 root노드로 하는 subtree 속에서 p또는 q가 존재하면 root노드를 반환하는 함수
        
        if root is None:
            return None

        # leaf node 부터 return해가며 타고 올라가는 느낌 - 재귀

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if root == p or root == q :
            return root
        
        elif left and right:
            return root
        
        elif left:
            return left
        elif right:
            return right
