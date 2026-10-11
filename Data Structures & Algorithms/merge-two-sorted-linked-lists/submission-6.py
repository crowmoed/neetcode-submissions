# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if (list1.val <= list2.val):
            retlist = ListNode(list1.val)
            list1=list1.next
        else:
            retlist = ListNode(list2.val)
            list2=list2.next
        tail = retlist
        while(list1 is not None and list2 is not None):
            if (list1.val <= list2.val):
                tail.next = ListNode(list1.val)
                tail = tail.next
                list1=list1.next
            else:
                tail.next = ListNode(list2.val)
                tail = tail.next
                list2=list2.next
                
        while(list1 is not None):
            tail.next = ListNode(list1.val)
            tail = tail.next
            list1=list1.next
        while(list2 is not None):
            tail.next = ListNode(list2.val)
            tail = tail.next
            list2=list2.next
        return retlist