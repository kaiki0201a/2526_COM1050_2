import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        listt = []
        heapq.heapify(listt)

        cur = 0
        while cur < len(lists):
            node = lists[cur]

            while node:

                heapq.heappush(listt, (node.val))
                node = node.next

            cur += 1
        
        dummy = ListNode()
        res = dummy
        while len(listt) > 0:

            node = ListNode(heapq.heappop(listt))
            dummy.next = node

            dummy = dummy.next
        
        return res.next
        