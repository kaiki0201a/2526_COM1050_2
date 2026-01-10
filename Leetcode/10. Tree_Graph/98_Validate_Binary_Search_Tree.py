#C1. Cap nhat can tren va can duoi
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bst(root, low, high):
            
            #if node == None: True
            if not root:
                return True

            if not(low < root.val < high):
                return False

            #Cap nhat can khi di chuyen ve ben trai va ben phai
            return bst(root.left, low, root.val) and bst(root.right, root.val, high)

        return bst(root, -float("inf"), +float("inf"))
    
#C2. In_Order, Left- Root- Right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        st = []

        #duyet het va bo vao st
        def bst(root):
            if not root:
                return

            bst(root.left)
            st.append(root.val)
            bst(root.right)

        bst(root)

        # Kiem tra xem cac phan tu trong st co tang dan hay khong
        i = 1
        while i < len(st):
            if st[i] <= st[i-1]:
                return False

            i += 1
        return True
