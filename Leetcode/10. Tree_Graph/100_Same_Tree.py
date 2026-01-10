# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
#Co 3 TH chinh:
- 2 None
<>
- 1 None
- 0 None
"""
#C1. Dung DFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #TH1: 2 None

        if not q and not p:  
            return True
        
        #TH2: 1 None, vi lenh if tren da loai di TH 2 none
        if not q or not p:
            return False
        
        if q.val != p.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#C2. Dung BFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        Q = deque()
        P = deque()
        
        if not q and not p:
            return True
        elif not q or not p:
            return False
        
        Q.append(q)
        P.append(p)

        while Q and P:
            node1 = Q.popleft()
            node2 = P.popleft()

            if node1.val != node2.val:
                return False
            
            if (node1.left and not node2.left) or (not node1.left and node2.left):
                return False
            
            if (node1.right and not node2.right) or (not node1.right and node2.right):
                return False
            
            if node1.left:
                Q.append(node1.left)
            if node2.left:
                P.append(node2.left)

            if node1.right:
                Q.append(node1.right)
            if node2.right:
                P.append(node2.right)

        return True

            