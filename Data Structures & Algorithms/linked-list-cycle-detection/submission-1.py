# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = head
        quick = head
        while tail is not None and quick is not None and quick.next is not None and quick.next.next is not None:
            tail =tail.next
            quick = quick.next.next
            if tail == quick:
                return True

            
        return False