# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next

        def print_node(node):
            temp = node
            while temp:
                print(temp.val)
                temp = temp.next
        
        def reverse(curr):
            prev = None
            while curr:
                nxt = curr.next
                curr.next=prev
                prev=curr
                curr=nxt
                if nxt:
                    nxt=nxt.next
            return prev

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None

        l1 = head
        l2 = reverse(curr)
        print_node(l1)
        print("**")
        print_node(l2)

        while l1 and l2:
            temp1, temp2 = l1.next, l2.next
            
            l1.next = l2
            if not temp2: 
                l2.next = temp1
                break
            l2.next = temp1
            l1 = temp1
            l2 = temp2


    
        # dummy = ListNode()
        # temp = dummy
        # ctr = 0
        # while l1 and l2:
        #     if ctr %2 == 0:
        #         temp.next = l1
        #         l1 = l1.next
        #     else:
        #         temp.next = l2
        #         l2 = l2.next
        #     temp = temp.next
        #     ctr+=1
        
        # if l1:
        #     temp.next = l1
        
        # if l2:
        #     temp.next = l2
        
        # return dummy.next

        



        

        