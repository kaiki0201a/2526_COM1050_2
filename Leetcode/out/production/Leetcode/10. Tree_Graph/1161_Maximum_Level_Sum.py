# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#YC: Level có tổng các phần tử max
#Ý tưởng: dùng BFS tính tổng

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        level, min_l = 0, 1

        q = dueue()
        q.append(root)

        while q:
            summ = 0

            #Lay het phan tu ra
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                summ += node.val
            level += 1

            if summ > res:
                res = summ
                min_l = level

        return min_l


                


