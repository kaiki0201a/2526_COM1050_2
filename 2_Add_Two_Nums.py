#EX for linked list
"""You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order,and each of their nodes contains a single digit
Add the two numbers and return the sum as a linked list.
"""
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode])
    -> Optional[ListNode]:
        #Step1: Creat a dummy note to start adding here
        dummy = ListNode()  #state
        cur = dummy     #use instead of dummy

        #Step2: Cal with l1 and l2
            #Determine value -> cal -> newnode -> linked to newnode
        while l1 or l2 or carry:    #l1,l2 != None, carry != 0
            #2.1 Determine value
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #cal newdigit
            val = v1 + v2 + carry

            carry = val // 10
            val = val%10
            cur.next = ListNode(val)

            #Update
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return Fake_Node.next
            
