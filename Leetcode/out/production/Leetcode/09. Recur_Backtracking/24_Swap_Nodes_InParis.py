#C1. Bien doi binh thuong
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Khoi tao
        dummy = ListNode(0, head)
        pre = dummy

        if head:
            cur = head
        else:
            return dummy.next
        
        #Bat dau vong lap
        while cur and cur.next:

            #Dinh nghia not can xu ly tiep truoc khi cat day
            nxt1 = cur.next
            nxt2 = cur.next.next

            #Noi day lai
            pre.next = nxt1     #Day 1: Pre noi vao nut 2
            cur.next = nxt2     #Day 2: Cur noi vao nut 3
            nxt1.next = cur     #Day 3: Noi nguoc lai

            #Di chuyen con tro
            pre = cur
            cur = nxt2

        return dummy.next
    
#C2: Recursive

#1. Decomposition
"""
Ta se swap tung cap va noi lai voi nhau
"""
#2. Base case
"""
Neu cur/ cur.next == None:  chi co 1 node con lai thi khong swap nua

"""

#Y tuong: ta se noi day nguoc lai 2->1 va 1 se noi voi phan can xu ly tiep theo
#Ta sẽ gọi hàm xử lý và nó sẽ trả về dần 






class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #Base case
        if not head or not head.next:
            return head

        #Lưu địa điểm
        nxt = head.next.next
    
        node2 = head.next   #Node dung sau
        node2.next = head   #Noi sau -> truoc

        head.next = self.swapPairs(nxt)  #Tim node ke tiep can xu noi


        #Noi node: """Day la phan can luu y nhat"""
        return node2

        
        
        

        
        

        
        
        
        















        
