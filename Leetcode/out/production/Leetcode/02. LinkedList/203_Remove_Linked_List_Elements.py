#Tim ki tu giong
#Xoa
#Ket noi
#Dung khi cham None

#C1: Tu lam, kha cong kenh
#Y tuong: tao ra mot node moi khi head.val != val thi ket noi vao
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        #Luu pre: != val ben trai
        
        pre = ListNode()
        dummy = pre


        while head:

            if head.val != val: #DK noi
                pre.next = head
                pre = pre.next

            #Xu ly node cuoi cung
            if not head.next and head.val == val:
                pre.next = head.next
            head = head.next

        return dummy.next

#C2. Gap cai giong thi shift qua
#Y tuong: truot: giong nhu sliding window
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev, cur = dummy, head

        while cur:
            nxt = cur.next  #Khai bao nhu nay thi khong can goi lai; se toi uu hon

            #NOTE!: Truot o day
            if cur.val == val:  #Neu cur.val == val, truot qua nxt(cur.next)
                prev.next = nxt

            else:   #Khi cur.val != val, thi previous cur == val hoac khong
                #Truot den diem khac val
                prev = prev.next
            
            cur = nxt
        
        return dummy.next
    
#C3:
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #1. Tao Dummy node 
        dummy = ListNode(0, head)

        #2. Con tro hien tai bat dau tu dummy
        curr = dummy

        #3. Duyet: chi can biet phia truoc con duong di ( next)
        while curr.next:
            if curr.next.val == val:
                # Cat day: Bo qua nut xau, noi thang toi nut sau no
                curr.next = cur.next.next
            else:
                # Neu nut tot, buoc den no
                curr = curr.next
        
        return dummy.next
    
#C4: Recursive

#1. Decomposition:
"""
Suppose moi danh sach chi gom hai phan:
- Head: Nut hien tai minh dang dung
- Rest: Tat ca cac nut phia sau head
    Tư duy: Tôi chỉ xử lý cái head còn phần rest sẽ là recur
"""
#2. Base case
"""
- Khi thay danh sach rong. Luc nay khong con gi de xoa, tra ve None

"""

#3.Abstraction
"""
- Gỉa sử hàm removeElements hoạt động đúng cho danh sách con phía sau
- Khi tôi gọi hàm nó sẽ trả cho tôi một cái đuôi sạch. Ta gán kq đó vào head.next
"""
#4. Algorithm
"""
- Sau khi phan duoi da sach, gio ta quay lai xet cai head( cur position)
+. Neu head la val: vut head di
+ Neu head != val: them head vao duoi
"""
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        #Base case
        if head is None:
            return None

        #Recursive Step - Di xu ly phan duoi truoc
        head.next = self.removeElements(head.next, val)

        #Xu ly nut hien tai
        if head.val == val:
            return head.next
        else:
            return head









        



