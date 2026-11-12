# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Y tuong: từ một root maxdepth của nó sẽ là maxdept của 2 subtree + 1

#C1. Recursive DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:    
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
#C2. Lever Order
# Ở một level ta sẽ pop hết ra và level +=1
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Base case
        if not root:
            return 0
        
        level = 0
        q = deque([root])

        while q:    

            for i in range(len(q)):     #Lay tat ca cua mot level ra vao them vao level moi
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.rihgt)

            level += 1

        return level

#C3.Iterative Pre Order Traversal (DFS)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([root.left, depth + 1])
                stack.append([root.right, depth +1])

        return res