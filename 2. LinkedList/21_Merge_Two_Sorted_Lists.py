# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#BEFORE CLEAN CODE
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        dummy = cur

        while list1 or list2:
            v1 = list1.val if list1 else None
            v2 = list2.val if list2 else None

            if v1 != None and v2 == None:   #v1 != None and v2 = None
                cur.next = list1
                break
            elif v1 == None and v2 != None:
                cur.next = list2
                break
            elif v1!= None and v2!= None:
                if v1 <= v2:
                    cur.next = ListNode(v1)
                    cur = cur.next

                    list1 = list1.next
                else:
                    cur.next = ListNode(v2)
                    cur = cur.next
                    list2 = list2.next                  
        return dummy.next
    
#AFTER CLEAN CODE
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        dummy = cur

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next

            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2                 
        return dummy.next