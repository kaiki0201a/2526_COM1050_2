#C1: Noob
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    listt = []

    while head != None:
        listt.append(head.val)
        head = head.next
        
    n = len(listt)
    if n == 0:
        return head
    cur = ListNode(listt[n-1])
    fake_node = cur

    for i in range(n-2, -1, -1):
        cur.next = ListNode(listt[i])
        cur = cur.next
        
    return fake_node

#C2: Pro: WHILE
# Pre -> Curr -> Next :----: Pre <- Cur <- Next
#B1.Xoá liên kết với node sau va thay vào đó là nối liên kết với trước
#Khi này cần lưu một biến để chứa node sau để còn chuyển node làm đến hết, suppose là nxt
#B2. Chuyển node: pre = cur, cur = next:    ghi đè tạm thời quên đi node vừa làm tý nối dây lại với nó sau

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    pre , cur = None, head

    while cur:

        #B1: Luu bien va noi day
        nxt = cur.next

        cur.next = pre  #Ngat day sau noi toi truoc
        #B2: chuyen node
        pre = cur
        cur = nxt

    return pre

#C3. Recursive
#Base case: head is None or head.next is None
#Giả sử head chư đảo ngược còn sau head đảo ngược hết rồi
#Ta sẽ nối head sao cho đúng là được
#Khi đó head.next == None: head là đuôi và head.next.next = head
def reversseList(head : Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    
    #new_head luu phan vau de quy xong ( phan da sap xep)
    new_head = self.reverssList(head.next)

    head.next.next = head
    head.next = None

    return new_head


