
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) :
        """
        Do not return anything, modify head in-place instead.
        """


        def recur(root):
            # 1. Xử lý trường hợp danh sách rỗng
            if not head:
                return None
            if head:
                current = head
            else:
                current = None
            du = None
            # 2. Duyệt đến khi node KẾ TIẾP là None
            # (Tức là current đang đứng ở node cuối cùng)
            while current.next: 
                du = current
                current = current.next
        
            return du, current


        #Bat dau tai head
        root = head
        while root:
            dummy = root    #Luu vi tri hien tai
            dummy2 = root.next  #Luu vi tri tiep theo

            pre_next, nextt = recur(root) #Truy van den cuoi
            if nextt == root.next or nextt == root :
                break
            pre_next.next = None
            print("CHECK: ",dummy.val, nextt.val)

            dummy.next = nextt
            nextt.next = dummy2

            root = dummy2
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

p1 = Solution()
p1.reorderList(a)

while a:
    print(a.val)
    a = a.next