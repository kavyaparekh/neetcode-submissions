# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #2 4 6 8
        second = slow.next #6
        prev = None 
        slow.next = None

        while second: 
            temp = second.next #8
            second.next = prev #None
            prev = second
            second = temp

        
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2


        