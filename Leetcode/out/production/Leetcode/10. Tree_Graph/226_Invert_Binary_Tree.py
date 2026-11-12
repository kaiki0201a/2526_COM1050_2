# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Y tuong: swap child -> swap cha

#C1: Recursive
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def rever(node):

            if not node:
                return

            node.left, node.right = node.right, node.left

            if node.left:
                rever(node.left)
            if node.right:
                rever(node.right)

        rever(root)

        return root
    

#C2:Su dung while va deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q = deque()
        q.append(root)

        while q:
            #Lay nut hien tai de xu ly
            node = q.popleft()

            #Swao child
            try:
                node.left, node.right = node.right, node.left
            except:
                continue

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root 