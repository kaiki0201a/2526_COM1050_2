# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#C1: Using hash set
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett = set()
        if not head or not head.next:
            return False
        while head:
            if head not in sett:
                sett.add(head)
            else:
                return True
            head = head.next
        return False
    
#C2: Rabbit and hare algorithm
def cycle(head: Opitiona[ListNode]):
    slow, fast = head, head

    while fast and fast.next:   #Dk la chua chua xong het
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

