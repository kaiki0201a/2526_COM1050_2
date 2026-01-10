def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    #trong hai truong hop chan, le deu tra ve dung slow
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow