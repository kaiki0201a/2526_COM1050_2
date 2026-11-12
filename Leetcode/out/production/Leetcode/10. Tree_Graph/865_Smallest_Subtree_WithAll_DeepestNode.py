#Y tuong: dung BFS tim ra cac node duoi cung roi lai tim cha chung cua cac node do
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Base case
        if not root:
            return
        
        #BFS tim cac node duoi cung
        q = deque()
        q.append(root)

        dictt = {}  #Dung de luu cac node cha

        while q:
            p = []  #Dung de chua cac node cuoi cung

            for i in range(len(q)):
                node = q.popleft()
                q.append(node)

                if node.left:   
                    q.append(node.left)
                    dictt[node.left] = node

                if node.right:
                    q.append(node.right)
                    dictt[node.right] = node


        #Dung ham search de tim xem co chung cha chua
        def search(node, target):
            if not node:
                return False
            if node == target:
                return True
        
            return search(node.left, target) or search(node.right, target)

        if len(p) <= 1:
            return node
        else:
            i = 0
            j = 1

            while j < len(p):
                if not search(dictt[p[i]], dictt[p[j]]):
                    dictt[p[i]] = dictt[dictt[p[i]]]
                else:
                    j += 1
        
        return dictt[p[0]]
                

